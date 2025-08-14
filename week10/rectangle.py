import pygame as pg

class GameRectangle:
    def __init__(self, window, color, x, y, w, h):
        self._window = window
        self._color = color
        self._rect = pg.Rect(x, y, w, h)

    def draw(self):
        pg.draw.rect(self._window, self._color, self._rect)

    def move_left(self, value):
        self._rect = pg.Rect(self._rect.left - value, self._rect.top, self._rect.width, self._rect.height)

    def move_right(self, value):
        self._rect = pg.Rect(self._rect.left + value, self._rect.top, self._rect.width, self._rect.height)
    
    def move_up(self, value):
        self._rect = pg.Rect(self._rect.left, self._rect.top - value, self._rect.width, self._rect.height)

    def move_down(self, value):
        self._rect = pg.Rect(self._rect.left, self._rect.top + value, self._rect.width, self._rect.height)

    def __str__(self):
        return f'{self._rect}'