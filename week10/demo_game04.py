from base_game import BaseGame
from rectangle import GameRectangle
import pygame as pg

class DemoGame(BaseGame):
    def __init__(self, width, height, title, bgcolor):
        super().__init__(width, height, title, bgcolor)
        self._speed = 10

    def _create_objects(self):
        color = pg.Color(100, 150, 200)
        self._rect = GameRectangle(self._window, color, 100, 100, 50, 50)

    def _draw_objects(self):
        self._rect.draw()

    def _handle_keydown(self, event):
        if event.key == pg.K_LEFT: self._rect.move_left(self._speed)
        elif event.key == pg.K_RIGHT: self._rect.move_right(self._speed)
        elif event.key == pg.K_UP: self._rect.move_up(self._speed)
        elif event.key == pg.K_DOWN: self._rect.move_down(self._speed)

### test game ###
if __name__ == "__main__":
    game = DemoGame(800, 600, "Demo Game", (255, 255, 255))
    game.game_loop()

