from typing import Callable

import pygame as pg
import pygame.event

from snakeGame.widgets.entity import Entity


class RoundedButton(Entity):
    def __init__(self, x, y, width, height, text, font_size, font_color, bg_color, border_color, border_width,
                 corner_radius=10, on_click: callable = lambda: None):
        super().__init__(x, y, width, height)

        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_width = border_width
        self.corner_radius = corner_radius

        self.font = pg.font.Font(None, font_size)

        self.on_click: callable = on_click
        self.clicked = False

    def draw(self, surface: pg.Surface):
        # Draw rounded rectangle
        pg.draw.rect(surface, self.bg_color, self.rect, border_radius=self.corner_radius)

        # Draw border
        pg.draw.rect(surface, self.border_color, self.rect, width=self.border_width, border_radius=self.corner_radius)

        # Render text
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event: pygame.event.Event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pg.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos) and self.clicked:
                if self.on_click:
                    self.on_click()
            self.clicked = False

