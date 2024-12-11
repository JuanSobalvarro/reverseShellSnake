import pygame as pg

from snakeGame.widgets.event_handler import EventHandler
from snakeGame.widgets.snake import Snake
from snakeGame.windows.window import Window
from snakeGame.widgets.dvdlike import DVDLike
from snakeGame.widgets.buttons import RoundedButton
from snakeGame.widgets.grid import Grid
from snakeGame.widgets.score_bar import ScoreBar

class PlayScreen(Window):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        # self.dvd_like = DVDLike(width=100, height=30, speed=80)
        # self.dvd_like2 = DVDLike(width=100, height=30, speed=80, x=100, y=100)
        self.score_bar = ScoreBar(screen_width // 3, screen_height // 10, screen_width // 3, screen_height // 10)
        self.grid = Grid(screen_width // 3, screen_height // 5, screen_width // 3, screen_height * 3 // 5, 10, 10)
        self.snake = Snake(self.grid, initial_pos=[0, 0], initial_length=3)

        self.event_handler = EventHandler()

    def load(self, return_menu: callable):
        self.event_handler.add_event(pg.KEYUP, lambda event: return_menu() if event.key == pg.K_ESCAPE else None)

        print("Loading play screen")
        self.add_widget(self.grid)
        self.add_widget(self.score_bar)
        self.add_widget(self.snake)

        # self.add_entity(self.event_handler)

        # self.add_entity(self.dvd_like)
        # self.add_entity(self.dvd_like2)
        print("Entities loaded: ", self._widgets)

    def unload(self):
        print("Unloading play screen")
        self.clear_widgets()
