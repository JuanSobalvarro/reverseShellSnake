import pygame as pg
from snakeGame.widgets.entity import Entity
from snakeGame.widgets.buttons import RoundedButton
from snakeGame.windows.window import Window


class Menu(Window):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)

        self.font = pg.font.Font(None, 70)

    def title(self):
        text_surface = self.font.render("Snake Game", True, (255, 255, 255))
        x = self.center[0] - text_surface.get_size()[0] // 2
        y = self.center[1] - text_surface.get_size()[1] * 6
        title = Entity(x, y, text_surface.get_size()[0], text_surface.get_size()[1])
        title.surface.blit(text_surface, (0, 0))

        self.add_entity(title)

    def buttons(self, on_play_click: callable):
        width, height = 200, 100
        x = self.center[0] - width // 2
        y = self.center[1] - height
        play_button = RoundedButton(x, y, width, height, "Play",
                                    50, (0, 0, 0), (0, 255, 0),
                                    (0, 190, 0), border_width=10,
                                    corner_radius=30, on_click=on_play_click)

        self.add_entity(play_button)

    def load(self, on_play_click: callable):
        print("Loading menu")
        self.title()
        self.buttons(on_play_click)
        print("Entities loaded: ", self._entities)

    def unload(self):
        print("Unloading menu")
        self.clear_entities()

