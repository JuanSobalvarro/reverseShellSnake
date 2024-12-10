import pygame as pg

from snakeGame.widgets.element import Element


class Entity:
    def __init__(self, x, y, width, height):
        self.surface = pg.Surface((width, height), pg.SRCALPHA)
        self.size = (width, height)
        self.x: float = x
        self.y: float = y
        self.rect = self.surface.get_rect(topleft=(x, y), width=width, height=height)
        self._elements: list[Element] = []

        self.clicked = False

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)

    def add_element(self, element):
        self._elements.append(element)

    def clear_elements(self):
        self._elements.clear()

    def draw(self, screen: pg.Surface):
        # print("Drawing entity with elements: ", self._elements)
        for element in self._elements:
            # print("Drawing element: ", element)
            element.draw(self.surface)

        screen.blit(self.surface, self.rect.topleft)

    def handle_event(self, event: pg.event.Event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.clicked = False


