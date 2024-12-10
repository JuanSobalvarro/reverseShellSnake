import pygame as pg

from snakeGame.widgets.animated_entity import AnimatedEntity
from snakeGame.widgets.element import Element

class DVDLike(AnimatedEntity):
    def __init__(self, x=0, y=0, width=50, height=50, speed=10):
        super().__init__(x, y, width, height, speed)
        self.color = (255, 0, 0)
        self.direction = [1.0, 1.0]

        self.body()

    def body(self):
        body = Element(self.rect.left, self.rect.top, self.rect.width, self.rect.height, self.color)
        text = pg.font.Font(None, 30).render("DVD UWU", True, (0, 0, 0))
        body.surface.blit(text, (0, 0))

        self.add_element(body)

    def update(self, screen: pg.Surface):
        time_delta = self.time_delta() / 1000

        dx = self.speed * time_delta * self.direction[0]
        dy = self.speed * time_delta * self.direction[1]
        self.move(dx, dy)
        self.handle_boundary_collision(screen)

        # print("DVDLike real position: ", self.get_position())

    def handle_boundary_collision(self, screen: pg.Surface):
        x_dir, y_dir = self.get_direction()
        x, y = self.get_position()
        new_x, new_y = x, y
        # print("===========================================")
        # print("DVDLike position: ", self.rect.topleft)
        # print("DVDLike direction: ", x_dir, y_dir)
        # print("Screen size: ", screen.get_size())

        if self.rect.right > screen.get_size()[0]:
            new_x = screen.get_size()[0] - self.rect.width
            x_dir *= -1
        elif self.rect.left < 0:
            new_x = 0
            x_dir *= -1

        if self.rect.bottom > screen.get_size()[1]:
            new_y = screen.get_size()[1] - self.rect.height
            y_dir *= -1
        elif self.rect.top < 0:
            new_y = 0
            y_dir *= -1

        self.set_position(new_x, new_y)
        # print("DVDLike new direction: ", x_dir, y_dir)
        self.set_direction((x_dir, y_dir))
