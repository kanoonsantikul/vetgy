import arcade
from models import Vetgy, Mouth, Model, ModelSprite
from random import randint, random

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
        self.sum_delta = 0
        self.score = 0

    def draw(self):
        self.upper_mouth.sprite.draw()
        self.lower_mouth.sprite.draw()

        self.noodle.sprite.draw()

        for vetgy in self.vetgies:
            vetgy.sprite.draw()

        arcade.draw_text(str(self.score),
                self.width - 60,
                30,
                arcade.color.BLACK, 20)

    def animate(self, delta):
        self.sum_delta += delta

        self.lower_mouth.animate(delta)
        self.noodle.y = self.lower_mouth.y - self.noodle.height / 2 + 110

        if self.sum_delta >= 1:
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
                    and vetgy.y + vetgy.height / 2 <= Mouth.MAX_Y + self.lower_mouth.height / 2):
                self.vetgies.remove(vetgy)
                self.score += 1

            if vetgy.y - vetgy.height / 2 >= self.height:
                self.vetgies.remove(vetgy)
