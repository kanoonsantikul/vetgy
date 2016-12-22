import arcade

from world import World

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

class MainWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(width, height)

    def on_draw(self):
        arcade.start_render()

        self.world.draw()

    def animate(self ,delta):
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = MainWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
