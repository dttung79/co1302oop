import pygame as pg

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

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # draw a rectangle
    pg.draw.rect(window, white, (200, 200, 100, 100))

    # draw a circle
    pg.draw.circle(window, a_color, (420, 240), 75)

    # update display (full-screen)
    pg.display.flip()