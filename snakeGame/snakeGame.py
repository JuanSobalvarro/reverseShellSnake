import pygame as pg

from snakeGame.game import Game
from snakeGame.windows.menu import Menu
from snakeGame.windows.play import PlayScreen

SCREEN_SIZE = (1280, 720)

class SnakeGame(Game):

    def __init__(self):
        super().__init__(SCREEN_SIZE[0], SCREEN_SIZE[1], "Snake Game")

        self.current_screen = None

        self.menu: Menu = Menu(SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.play_screen: PlayScreen = PlayScreen(SCREEN_SIZE[0], SCREEN_SIZE[1])

        self.activate_fps_counter()

        self.load_menu()


    @staticmethod
    def load_current_screen(foo):
        def wrapper(self, *args, **kwargs):
            if self.current_screen:
                self.current_screen.unload()
            return foo(self, *args, **kwargs)
        return wrapper

    @load_current_screen
    def load_menu(self):

        print("Loading Menu")
        self.menu.load(self.load_play_screen)
        print("Menu entities: ", self.menu.get_entities())
        self.load_entities(self.menu.get_entities())

        self.current_screen = self.menu

    @load_current_screen
    def load_play_screen(self):
        print("Loading Play Screen")
        self.play_screen.load()
        self.load_entities(self.play_screen.get_entities())

        self.current_screen = self.play_screen

    def activate_fps_counter(self):
        self.count_fps = True
        self.fps_counter_delay = 0.3
