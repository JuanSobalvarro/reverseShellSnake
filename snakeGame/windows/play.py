import pygame as pg
from snakeGame.widgets.entity import Entity
from snakeGame.widgets.buttons import RoundedButton
from snakeGame.windows.window import Window


class PlayScreen(Window):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)

    def load(self):
        pass