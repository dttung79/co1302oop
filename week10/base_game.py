import pygame as pg
from abc import ABC, abstractmethod

class BaseGame(ABC):
    def __init__(self, width, height, title, bgcolor):
        self._width = width
        self._height = height
        self._bgcolor = bgcolor

        pg.init()
        pg.display.set_caption(title)
        self._window = pg.display.set_mode((self._width, self._height))
        self._fps = pg.time.Clock()

        self._create_objects()

    @abstractmethod
    def _create_objects(self):
        pass

    def game_loop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                # handle key down events
                elif event.type == pg.KEYDOWN:
                    self._handle_keydown(event)

            # handle key press
            keys = pg.key.get_pressed()
            self._handle_keypress(keys)

            # clear the screen
            self._window.fill(self._bgcolor)

            # draw game objects
            self._draw_objects()

            # update the display
            pg.display.flip()
            self._fps.tick(60)

    def _handle_keydown(self, event):
        pass

    def _handle_keypress(self, keys):
        pass
    
    @abstractmethod
    def _draw_objects(self):
        pass
