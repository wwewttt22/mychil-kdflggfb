from pygame import*
from gamesprite import *
from platforma import *


WINDOWSIZE = (800,600)

TXTCOLOR = (134,74,249)
BGCOLOR = (248,229,89)

window = display.set_mode(WINDOWSIZE)
display.set_caption('pinpon')

timer = time.Clock()
run = True


platform_left = Platform('platformaaa.png',10,250,200,200,5,window)
platform_right = Platform('platformaaa.png',500,250,200,200,5,window)



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(BGCOLOR)

    platform_left.reset()
    platform_left.update_left()
    platform_right.reset()
    platform_right.update_right()

    display.update()
    timer.tick(60)








