import pygame as pg

from snakeGame.widgets.entity import Entity


class EventHandler(Entity):
    def __init__(self):
        super().__init__(0, 0, 0, 0)
        self._events = {}

    def add_event(self, event_type, callback: callable):
        self._events[event_type] = callback

    def handle_events(self, event: pg.event.Event):
        if event.type in self._events:
            self._events[event.type](event)