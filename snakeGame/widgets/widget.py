import pygame as pg


class Widget:
    def __init__(self, screen: pg.Surface, x, y, width, height):
        self.screen = screen
        self.surface = pg.Surface((width, height), pg.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=(x, y), width=width, height=height)
        self.size = (width, height)
        self.x: float = x
        self.y: float = y

        self.last_update_time = pg.time.get_ticks()

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)

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
        the animation correctly, this method should be called every time the game loop updates
        :param screen:
        :return:
        """
        time_delta = self.time_delta()

        dx = time_delta
        dy = time_delta
        self.move(dx, dy)

    def move(self, dx, dy):
        self.set_position(self.x + dx, self.y + dy)

    def draw(self):
        # print("Drawing widget", self, " at: ", self.rect.topleft)
        self.screen.blit(self.surface, self.rect.topleft)

    def handle_event(self, event: pg.event.Event):
        """
        Handle events for the entity, you may want to override this method to handle the events
        :param event:
        :return:
        """
        pass

