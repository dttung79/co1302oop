from base_game import BaseGame
from rectangle import GameRectangle
from circle import GameCircle
import pygame as pg
import random as rd

class DropingEggs(BaseGame):
    def __init__(self):
        super().__init__(800, 600, "Droping Eggs", (255, 255, 255))
        self._egg_speed = 10
        self._basket_speed = 10
        self._score = 0
        self._lives = 3

    def _show_score_lives(self):
        font = pg.font.Font(None, 36)
        score_color = pg.Color(255, 0, 0)  # red color for text
        text_score = font.render(f"Score: {self._score}", True, score_color)
        self._window.blit(text_score, (10, 10))   # show score at (10, 10) on window
        lives_color = pg.Color(0, 0, 255)  # blue color for text
        text_lives = font.render(f"Lives: {self._lives}", True, lives_color)
        self._window.blit(text_lives, (10, 40))   # show lives at (10, 40) on window

    def _create_egg(self):
        # create an egg
        egg_x = rd.randint(50, self._width - 50)
        egg_y = 25
        egg_color = (rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
        egg_radius = 25
        return GameCircle(self._window, egg_color, egg_x, egg_y, egg_radius)

    def _create_basket(self):
        basket_x = self._width // 2 - 50
        basket_y = self._height - 50
        basket_color = (0, 0, 255)
        basket_width = 100
        basket_height = 20
        return GameRectangle(self._window, basket_color, basket_x, basket_y, basket_width, basket_height)
    
    def _create_ground(self):
        ground_color = (0, 255, 0)
        ground_y = self._height - 10
        return GameRectangle(self._window, ground_color, 0, ground_y, self._width, 10)
    
    def _create_objects(self):
        self._egg = self._create_egg()
        self._basket = self._create_basket()
        self._ground = self._create_ground()

    def _draw_objects(self):
        self._egg.draw()
        self._basket.draw()
        self._ground.draw()

        self._show_score_lives()  # show score on window

        self._egg.move_down(self._egg_speed)
        # check if egg touch the ground
        if self._egg._border.bottom >= self._ground._rect.top:
            self._lives -= 1
            if self._lives <= 0:
                self._game_over()
            else:
                # reset egg position
                self._egg = self._create_egg()

    def _game_over(self):
        text_color = pg.Color(0, 0, 0)
        text_font = pg.font.Font(None, 74)
        text = "Game Over"
        text_surface = text_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=(self._width // 2, self._height // 2))
        self._window.blit(text_surface, text_rect)
        pg.display.flip()
        pg.time.wait(2000)
        pg.quit()

    def _handle_keypress(self, keys):
        if keys[pg.K_LEFT]:
            self._basket.move_left(self._basket_speed)
        elif keys[pg.K_RIGHT]:
            self._basket.move_right(self._basket_speed)
        
        if self._egg_touch_basket():
            self._score += 1
            self._egg = self._create_egg()  # reset egg
    
    def _egg_touch_basket(self):
        # check if egg touches the basket
        return self._egg._border.colliderect(self._basket._rect)

if __name__ == "__main__":
    game = DropingEggs()
    game.game_loop()