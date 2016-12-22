import arcade.key
import arcade
from models import Vetgy, Mouth, Model, ModelSprite
from random import randint, random, uniform

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.noodle = Model(
                self,
                self.width / 2,
                self.height / 2 - 85,
                'images/noodle.png', 0)

        self.upper_mouth = Model(
                self,
                self.width / 2,
                self.height,
                'images/upper-mouth.png', 0)
        self.upper_mouth.y -= self.upper_mouth.height / 2
        self.lower_mouth = Mouth(
                self,
                self.width / 2,
                Mouth.MAX_Y)

        self.lives = []
        y = 30
        for live in range(3):
            live = Model(self, 30, y, 'images/live.png', 0)
            y += 50
            self.lives.append(live)

        self.vetgies = []
        self.selection = 0
        self.sum_delta = 0
        self.score = 0
        self.is_gameover = False

    def draw_game(self):
        self.upper_mouth.sprite.draw()
        self.lower_mouth.sprite.draw()

        self.noodle.sprite.draw()

        for vetgy in self.vetgies:
            vetgy.sprite.draw()

        for live in self.lives:
            live.sprite.draw()

        arcade.draw_text(str(self.score),
                self.width - 60,
                30,
                arcade.color.BLACK, 20)

    def draw_gameover(self):
        arcade.draw_text("GAME OVER",
                20,
                self.height / 2,
                arcade.color.BLACK, 20)

    def draw(self):
        if self.is_gameover:
            self.draw_gameover()
        else:
            self.draw_game()

    def animate(self, delta):
        self.lower_mouth.animate(delta)
        self.noodle.y = self.lower_mouth.y - self.noodle.height / 2 + 110

        self.sum_delta += delta
        if self.sum_delta >= uniform(1.4, 1.8):
            noodle_width = (int)(self.noodle.width / 2)
            vetgy = Vetgy(
                    self,
                    randint(
                            self.width / 2 - noodle_width,
                            self.width / 2 + noodle_width),
                    -20)
            self.vetgies.append(vetgy)

            self.sum_delta = 0

        for vetgy in self.vetgies:
            vetgy.animate(delta)

            if (vetgy.y - vetgy.height / 2 >= self.lower_mouth.y + self.lower_mouth.height / 2 - 15
                    and vetgy.y + vetgy.height / 2 - 15 <= Mouth.MAX_Y + self.lower_mouth.height / 2):
                self.vetgies.remove(vetgy)
                if self.selection != 0:
                    self.selection -= 1
                vetgy.sprite.kill()
                self.score += 1

            if vetgy.y - vetgy.height / 2 >= self.height:
                self.vetgies.remove(vetgy)
                if self.selection != 0:
                    self.selection -= 1
                vetgy.sprite.kill()

                if len(self.lives) > 0:
                    live = self.lives.pop()
                    live.sprite.kill()

        if len(self.vetgies) > self.selection:
            self.vetgies[self.selection].select()

        if len(self.lives) <= 0:
            self.is_gameover = True

    def on_key_press(self, key, key_modifiers):
            if key == arcade.key.UP:
                if len(self.vetgies) > self.selection:
                    self.vetgies[self.selection].turbo()

            if key == arcade.key.DOWN:
                if len(self.vetgies) > self.selection:
                    self.vetgies[self.selection].slow()

            if key == arcade.key.LEFT:
                if (len(self.vetgies) > self.selection - 1
                        and self.selection - 1 >= 0):
                    self.vetgies[self.selection].deselect()
                    self.selection -= 1
                    self.vetgies[self.selection].select()

            if key == arcade.key.RIGHT:
                if (len(self.vetgies) > self.selection + 1
                        and self.selection + 1 < len(self.vetgies)):
                    self.vetgies[self.selection].deselect()
                    self.selection += 1
                    self.vetgies[self.selection].select()

    def on_key_release(self, key, key_modifiers):
            if key == arcade.key.UP or key == arcade.key.DOWN:
                if len(self.vetgies) > self.selection:
                    self.vetgies[self.selection].speed = Vetgy.SPEED
