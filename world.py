from models import Noodle, Vetgy
from random import randint, random
import setting

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.noodle = Noodle(
                self,
                setting.SCREEN_WIDTH / 2,
                setting.SCREEN_HEIGHT / 2)

        self.vetgies = []
        for i in range(5):
            vetgy = Vetgy(self,
                    randint(0, setting.SCREEN_WIDTH),
                    -20)
            self.vetgies.append(vetgy)

    def draw(self):
        self.noodle.sprite.draw()
        for vetgy in self.vetgies:
            vetgy.sprite.draw()

    def animate(self, delta):
        for vetgy in self.vetgies:
            vetgy.animate(delta)
