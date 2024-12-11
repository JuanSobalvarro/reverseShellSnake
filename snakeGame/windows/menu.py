import pygame as pg
import sys

from snakeGame.widgets.widget import Widget
from snakeGame.widgets.buttons import RoundedButton
from snakeGame.windows.window import Window


class Menu(Window):
    def __init__(self, screen: pg.Surface, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)

        self.font = pg.font.Font(None, screen_width // 8)

    def title(self):
        text_surface = self.font.render("Snake Game", True, (255, 255, 255))
        x = self.center[0] - text_surface.get_size()[0] // 2
        y = self.center[1] - text_surface.get_size()[1] - self.screen_height // 4
        title = Widget(self.get_screen(), x, y, text_surface.get_size()[0], text_surface.get_size()[1])
        title.surface.blit(text_surface, (0, 0))

        self.add_widget(title)

    def buttons(self, on_play_click: callable):
        self.add_widget(self.play_button(on_play_click))
        self.add_widget(self.exit_button(lambda: sys.exit()))

    def play_button(self, callback: callable) -> RoundedButton:
        width, height = self.screen_width // 3, self.screen_height // 5
        x = self.center[0] - width // 2
        y = self.center[1] - height
        print("Play button at: ", x, y)
        play_button = RoundedButton(self.get_screen(), x, y, width, height, "Play",
                                    width // 4, (0, 0, 0), (0, 255, 0),
                                    (0, 190, 0), border_width=10,
                                    corner_radius=height // 3, on_click=callback)

        return play_button

    def exit_button(self, callback: callable) -> RoundedButton:
        width, height = self.screen_width // 5, self.screen_height // 5
        x = self.center[0] - width // 2
        y = self.center[1] + height // 6
        exit_button = RoundedButton(self.get_screen(), x, y, width, height, "Exit",
                                    width // 3, (255, 255, 255), (100, 100, 100),
                                    (50, 50, 50), border_width=10,
                                    corner_radius=height // 3, on_click=callback)
        return exit_button

    def load(self, on_play_click: callable):
        print("Loading menu")
        self.title()
        self.buttons(on_play_click)
        print("Widgets loaded: ", self._widgets)

    def unload(self):
        print("Unloading menu")
        self.clear_widgets()

    def draw(self):
        # print("Drawing menu")
        for widget in self._widgets:
            widget.draw()

    def handle_window_event(self, event: pg.event.Event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                sys.exit()

