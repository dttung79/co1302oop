import pygame as pg
from rectangle import GameRectangle
# define game window dimensions
width = 640
height = 480

# define some colors
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
a_color = pg.Color(100, 150, 200)

# init game
pg.init()
pg.display.set_caption("Demo Game 01")

# create game window
window = pg.display.set_mode((width, height))
fps = pg.time.Clock()

r = GameRectangle(window, a_color, 100, 100, 50, 50)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT: r.move_left(5)
            elif event.key == pg.K_RIGHT: r.move_right(5)
            elif event.key == pg.K_UP: r.move_up(5)
            elif event.key == pg.K_DOWN: r.move_down(5)
    # fill the window with black color
    pg.draw.rect(window, black, (0, 0, width, height))

    r.draw()    
    
    fps.tick(60)  # Limit the frame rate to 60 FPS
    pg.display.update()  # Update the display