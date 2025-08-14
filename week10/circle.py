import pygame as pg

class GameCircle:
    def __init__(self, window, color, x, y, radius):
        self._window = window
        self._color = color
        self._border = pg.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def draw(self):
        pg.draw.circle(self._window, self._color, self._border.center, self._border.width // 2)

    def move_left(self, value):
        self._border.x -= value

    def move_right(self, value):
        self._border.x += value
    
    def move_up(self, value):
        self._border.y -= value

    def move_down(self, value):
        self._border.y += value