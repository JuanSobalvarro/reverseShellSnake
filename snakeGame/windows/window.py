import pygame as pg

from snakeGame.widgets.entity import Entity


class Window:
    def __init__(self, screen_width: int, screen_height: int):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.center = (self.screen_width / 2, self.screen_height / 2)

        self._entities: list[Entity] = []

    # This method SHOULD be overridden by subclasses
    def load(self):
        pass

    # Override this method if you need to clear different things than entities
    def unload(self):
        self.clear_entities()

    def add_entity(self, entity):
        self._entities.append(entity)

    def clear_entities(self):
        self._entities.clear()

    def get_entities(self):
        return self._entities

    def handle_event(self, event: pg.event.Event):
        """
        Handle events for all entities in the window
        :param event:
        :return:
        """
        for entity in self._entities:
            # print("Handling event for entity: ", entity)
            entity.handle_event(event)