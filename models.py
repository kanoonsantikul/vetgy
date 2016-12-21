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
    def __init__(self, world, x, y, sprite_path, angle):
        self.world = world
        self.x = x
        self.y = y
        self.sprite = ModelSprite(sprite_path, model=self)
        self.width = self.sprite.texture.width
        self.height = self.sprite.texture.height
        self.angle = 0

    def hit(self, other):
        return ((abs(self.x - other.x) <= (self.width / 2 + other.width / 2)) and
                (abs(self.y - other.y) <= (self.height / 2 + other.height / 2)))

class Vetgy(Model):
    SPEED = 5

    def __init__(self, world, x, y):
        super().__init__(
                world, x, y,
                'images/vetgy.png', 0)

    def animate(self, delta):
        self.y += Vetgy.SPEED

class Mouth(Model):
    MAX_Y = 550
    MIN_Y = 450
    SPEED = 2

    def __init__(self, world, x, y):
        super().__init__(
                world, x, y,
                'images/lower-mouth.png', 0)

        self.velocity = -Mouth.SPEED

    def animate(self, delta):
        if self.y > Mouth.MAX_Y or self.y < Mouth.MIN_Y:
            self.velocity = -self.velocity

        self.y += self.velocity
