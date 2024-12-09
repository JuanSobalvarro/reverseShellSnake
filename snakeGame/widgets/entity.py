import pygame as pg


class Entity:
    def __init__(self, x, y, width, height):
        self.surface = pg.Surface((width, height), pg.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=(x, y), width=width, height=height)

        self._elements = []

        self.clicked = False

    def add_element(self, element):
        self._elements.append(element)

    def draw(self, screen: pg.Surface):
        for element in self._elements:
           element.draw(self.surface)

        screen.blit(self.surface, self.rect.topleft)

    def handle_event(self, event: pg.event.Event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.clicked = False