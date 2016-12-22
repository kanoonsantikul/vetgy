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

        self.vetgies = []
        self.selection = 0
        self.sum_delta = 0
        self.score = 0

    def draw(self):
        self.upper_mouth.sprite.draw()
        self.lower_mouth.sprite.draw()

        self.noodle.sprite.draw()

        for vetgy in self.vetgies:
            vetgy.sprite.draw()

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

        if len(self.vetgies) > self.selection:
            self.vetgies[self.selection].select()

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
