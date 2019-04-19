"""
(c) Andrew Shen 2019

Neuron.py
    This is where are all the "neuron"s are. Which are technically objects.
    And is where the Neurons are and the built-in functionality are
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
