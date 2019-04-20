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

import pygame as p
import ctypes as c
c.windll.user32.SetProcessDPIAware()

from source.ProjectManager import ProjectManager as ProjectM
from source import GUI
from source.Neuron import Node

# basic pygame set-up
p.init()
SCREEN = (1920, 1080)
#SURF = p.display.set_mode((0, 0), p.FULLSCREEN)
SURF = p.display.set_mode((500, 500))
p.display.set_caption("GUI AI")
CLOCK = p.time.Clock()
FPS = 60
LOOP = True

# set-up
proj = ProjectM("test.gai")
cnst = proj.CONSTANT

MOUSE_DATA = [[0, 0], [0, 0]]  # [pos], [lClick, rClick]
O_LIST = []  # [[Neuron, POS]]; Object List
SELECTED = None  # selected node

but1 = GUI.Button((0, 0, 100, cnst["settings"]["MENU_HEADER"]), "+Node")

while LOOP:
    for e in p.event.get():
        if e.type == p.QUIT: LOOP = False
        elif e.type == p.MOUSEBUTTONDOWN:
            if e.button == 1: MOUSE_DATA[1][0] = 1
            elif e.button == 3: MOUSE_DATA[1][1] = 1
            for o in O_LIST:
                #print(pos[0], MOUSE_DATA[0][0])
                if ((abs(o.pos[0]-MOUSE_DATA[0][0]))**2)+(abs(o.pos[1]-MOUSE_DATA[0][1])**2) <= cnst["object"]["NODE_SIZE"]**2:  # select items
                    print(True)
                    o.SELECTED = True

        elif e.type == p.MOUSEBUTTONUP:
            if e.button == 1: MOUSE_DATA[1][0] = 0
            elif e.button == 3: MOUSE_DATA[1][1] = 0
            for o in O_LIST:  # unselect items
                if o.SELECTED is True:
                    o.SELECTED = False
                    o.update(MOUSE_DATA[0])

        elif e.type == p.MOUSEMOTION:
            MOUSE_DATA[0] = [e.pos[0], e.pos[1]]
        elif e.type == p.KEYDOWN:
            if e.key == p.K_ESCAPE: LOOP = False

    SURF.fill((225, 225, 150))

    p.draw.rect(SURF, (100, 100, 100), (0, 0, SCREEN[0], cnst["settings"]["MENU_HEADER"]))  # menu
    but1.render(SURF)

    for o in O_LIST:  # selected items
        if o.SELECTED is True:
            o.update(MOUSE_DATA[0])

    if but1.update(MOUSE_DATA[0], MOUSE_DATA[1][0]):
        O_LIST.append(Node(cnst["object"]["NODE_SIZE"], "f(x)", MOUSE_DATA[0]))
        O_LIST[-1].SELECTED = True

    for o in O_LIST:
        o.render(SURF)

    print(O_LIST)

    p.display.flip()
    CLOCK.tick(FPS)