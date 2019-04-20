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

p.init()

class Neuron:
    def __init__(self):
        pass


class Node:
    SELECTED = False

    def __init__(self, sz, fx, pos):
        self.size = sz
        self.fx = fx
        self.pos = pos
        self.amnt = 0

    def update(self, pos, **kwargs):
        self.pos = pos
        for kw, val in kwargs.items():
            if kw == "amount": self.amnt = val

    def render(self, surf):
        p.draw.circle(surf, (0, 0, 0), self.pos, 20)
