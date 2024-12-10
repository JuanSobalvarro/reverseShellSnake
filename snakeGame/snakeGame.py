import pygame as pg

from snakeGame.game import Game
from snakeGame.windows.menu import Menu
from snakeGame.windows.play import PlayScreen

SCREEN_SIZE = (1280, 720)

class SnakeGame(Game):

    def __init__(self):
        super().__init__(SCREEN_SIZE[0], SCREEN_SIZE[1], "Snake Game")

        self.menu: Menu = Menu(SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.play_screen: PlayScreen = PlayScreen(SCREEN_SIZE[0], SCREEN_SIZE[1])

        self.activate_fps_counter()
        self.activate_mouse_position()

        self.load_menu()

    # When loading a screen load a function as load_"screen_name" and use this decorator
    @staticmethod
    def load_current_screen(foo):
        def wrapper(self, *args, **kwargs):
            if self.current_screen:
                self.current_screen.unload()
            foo(self, *args, **kwargs)
            self.current_screen = getattr(self, foo.__name__[5:])

        return wrapper

    @load_current_screen
    def load_menu(self):
        self.menu.load(self.load_play_screen)
        self.load_entities(self.menu.get_entities())

    @load_current_screen
    def load_play_screen(self):
        self.play_screen.load(self.load_menu)
        self.load_entities(self.play_screen.get_entities())

    def activate_fps_counter(self):
        self.count_fps = True
        self.fps_counter_delay = 0.3

    def activate_mouse_position(self):
        self.mouse_pos = True
