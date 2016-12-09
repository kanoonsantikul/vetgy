import arcade

from models import World

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

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

class MainWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(width, height)

    def on_draw(self):
        arcade.start_render()

    def animate(self ,delta):
        self.world.animate(delta)

if __name__ == '__main__':
    window = MainWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
