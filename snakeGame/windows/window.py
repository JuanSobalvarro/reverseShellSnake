import pygame as pg


class Window:
    def __init__(self, screen_width: int, screen_height: int):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.center = (self.screen_width / 2, self.screen_height / 2)

        self._entities = []

    # This method SHOULD be overridden by subclasses
    def load(self):
        pass

    # Override this method if you need to clear different things than entities
    def unload(self):
        self._entities.clear()

    def add_entity(self, entity):
        self._entities.append(entity)

    def clear_entities(self):
        self._entities.clear()

    def get_entities(self):
        return self._entities