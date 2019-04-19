# All the GUI Class and functionalities

from src import base as b

import pygame as p
p.init()


class Button:
    CLICKED = False

    def __init__(self, rect, text, *args):  # rect: (posx, posy, szx, szy), text, arg[0]: backColor, arg[1]: foreColor
        self.rect = rect
        self.txt = p.font.SysFont("arial", 24).render(text, True, b.check_args(0, (255, 220, 150), args) )
        self.backg = b.check_args(0, (100, 100, 255), args)

    def update(self, pos, button):
        if (self.rect[0] <= pos[0] <= self.rect[2]) and (self.rect[1] <= pos[1] <= self.rect[3]) and button == 1 and Button.CLICKED == False:
            Button.CLICKED = True
            return True
        elif button == 0 and Button.CLICKED == True:
            Button.CLICKED = False
            return False

    def render(self, surf):  # surface
        p.draw.rect(surf, self.backg, self.rect)
        surf.blit(self.txt, (self.rect[0], self.rect[1]) )