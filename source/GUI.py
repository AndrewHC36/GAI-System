"""
Copyright (C) 2019  Andrew Shen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# All the GUI Class and functionalities

from source import base as b

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