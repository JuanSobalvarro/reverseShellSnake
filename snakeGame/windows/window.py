import pygame as pg

from snakeGame.widgets.widget import Widget


class Window:
    def __init__(self, screen: pg.Surface, screen_width: int, screen_height: int):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.center = (self.screen_width / 2, self.screen_height / 2)

        self._widgets: list[Widget] = []

    def get_screen(self):
        return self.screen

    # This method SHOULD be overridden by subclasses
    def load(self):
        pass

    # Override this method if you need to clear different things than entities
    def unload(self):
        self.clear_widgets()

    def add_widget(self, entity):
        self._widgets.append(entity)

    def clear_widgets(self):
        self._widgets.clear()

    def get_widgets(self):
        return self._widgets

    def draw(self):
        for widget in self._widgets:
            widget.draw()

    def handle_widgets_event(self, event: pg.event.Event):
        """
        Handle events for the widgets
        :param event:
        :return:
        """
        for widget in self._widgets:
            # print("Handling event for widget: ", widget)
            widget.handle_event(event)

    def handle_window_event(self, event: pg.event.Event):
        """
        Handle events for the window, like general events as pressing the ESC key, etc. This method should be
        overridden by subclasses
        :param event:
        :return:
        """
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                self.unload()

    def handle_event(self, event: pg.event.Event):
        """
        Handle event for the window and then for the widgets. This method should be called by the game loop
        when processing events
        :param event:
        :return:
        """
        self.handle_window_event(event)
        self.handle_widgets_event(event)