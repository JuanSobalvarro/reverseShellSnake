from typing import Tuple

import pygame as pg
from snakeGame.widgets.entity import Entity

class AnimatedEntity(Entity):
    def __init__(self, x, y, width, height, speed: float = 1):
        super().__init__(x, y, width, height)
        self.speed = speed  # speed in pixels per ms
        self.direction = [1.0, 1.0]
        self.last_update_time = pg.time.get_ticks()

    def time_delta(self) -> int:
        """
        Get the time delta(ms) since the last update
        :return:
        """
        last_time = self.last_update_time
        self.last_update_time = pg.time.get_ticks()
        return pg.time.get_ticks() - last_time

    def update(self, screen: pg.Surface):
        """
        Update the position of the entity, this is the method you maybe want to override to handle
        the animation correctly
        :param screen:
        :return:
        """
        time_delta = self.time_delta()

        dx = self.speed * time_delta * self.direction[0]
        dy = self.speed * time_delta * self.direction[1]
        self.move(dx, dy)
        # self.handle_boundary_collision(screen)

    def move(self, dx, dy):
        self.set_position(self.x + dx, self.y + dy)

    def handle_boundary_collision(self, screen: pg.Surface):
        pass

    def set_direction(self, direction: Tuple[float, float]):
        self.direction = list(direction)

    def get_direction(self):
        return tuple(self.direction)

    def draw(self, screen: pg.Surface):
        # print("Drawing animated entity")
        self.update(screen)
        for element in self._elements:
            element.draw(self.surface)

        screen.blit(self.surface, self.rect.topleft)