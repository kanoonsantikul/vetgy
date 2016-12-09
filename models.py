import arcade.key

from random import randint, random

class Model:
    def __init__(self, world, x, y, width, height, angle):
        self.world = world
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = 0

    def hit(self, other):
        return ((abs(self.x - other.x) <= (self.width / 2 + other.width / 2)) and
                (abs(self.y - other.y) <= (self.height / 2 + other.height / 2)))

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def animate(self, delta):
        self
