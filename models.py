import arcade.key

from random import randint, random

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()

class Model:
    def __init__(self, world, x, y, sprite, angle):
        self.world = world
        self.x = x
        self.y = y
        self.sprite = sprite
        self.width = sprite.texture.width
        self.height = sprite.texture.height
        self.angle = 0

    def hit(self, other):
        return ((abs(self.x - other.x) <= (self.width / 2 + other.width / 2)) and
                (abs(self.y - other.y) <= (self.height / 2 + other.height / 2)))

class Noodle(Model):
    def __init__(self, world, x, y):
        super().__init__(
                world, x, y,
                ModelSprite('images/noodle.png', model=self), 0)

class Vetgy(Model):
    SPEED = 5

    def __init__(self, world, x, y):
        super().__init__(
                world, x, y,
                ModelSprite('images/vetgy.png', model=self), 0)

    def animate(self, delta):
        self.y += Vetgy.SPEED
