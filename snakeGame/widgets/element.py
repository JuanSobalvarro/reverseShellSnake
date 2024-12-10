import pygame as pg

class Element:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.surface = pg.Surface((width, height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()

    def draw(self, screen: pg.Surface):
       screen.blit(self.surface, (self.x, self.y))

    def __repr__(self):
        return f"Element(x={self.x}, y={self.y}, rect={self.rect})"
