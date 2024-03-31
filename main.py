from pygame import*
from gamesprite import *



WINDOWSIZE = (800,600)

TXTCOLOR = (134,74,249)
BGCOLOR = (248,229,89)

window = display.set_mode(WINDOWSIZE)
display.set_caption('pinpon')

timer = time.Clock()
run = True





while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill(BGCOLOR)    
    display.update()
    timer.tick(60)








