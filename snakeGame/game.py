from math import inf
import asyncio
import time

import pygame as pg

from snakeGame.widgets.widget import Widget
from snakeGame.windows.window import Window


class Game:
    def __init__(self, width: int, height: int, title: str):
        pg.init()
        self.running = False
        self.screen: pg.Surface = pg.display.set_mode(size = (width, height))
        self.clock: pg.time.Clock = pg.time.Clock()
        pg.display.set_caption(title=title)

        # Fps related
        self.count_fps: bool = False
        self.fps_counter_delay: float = 1
        self._last_fps_update = time.time()
        self.fps = 0

        self.mouse_pos: bool = False

        self.current_window: Window = None

    def get_screen(self):
        return self.screen

    def run(self, fps: int = inf):
        self.running = True
        asyncio.run(self._main_loop(fps))

    async def events(self):
        # print("Handling events for screen: ", self.current_screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if isinstance(self.current_window, Window) and hasattr(self.current_window, 'handle_event'):
                # print("Handling event for screen: ", self.current_window)
                self.current_window.handle_event(event)

    def _render_mouse_position(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_pos_surface = pg.font.Font(None, 20).render(f"Mouse position: {mouse_pos}", True, (255, 255, 255))
        self.screen.blit(mouse_pos_surface, (0, 0))

    def _render_fps(self):
        current_time = time.time()
        if current_time - self._last_fps_update >= self.fps_counter_delay:
            self.fps = self.clock.get_fps()
            self._last_fps_update = current_time
        fps_surface = pg.font.Font(None, 20).render(f"FPS: {self.fps:.2f}", True, (255, 255, 255))
        self.screen.blit(fps_surface, (self.screen.get_width() - fps_surface.get_size()[0], 0))

    def _render_game(self):

        # Wipe screen to clean last frame
        self.screen.fill("black")

        # Render game
        if self.current_window:
            self.current_window.draw()

        if self.count_fps:
            self._render_fps()

        if self.mouse_pos:
            self._render_mouse_position()


    async def _main_loop(self, framerate_limit = inf):
        loop = asyncio.get_event_loop()

        next_frame_target = 0.0
        limit_frame_duration = (1.0 / framerate_limit)

        while self.running:

            # framerate limiter
            if limit_frame_duration:
                this_frame = time.time()
                delay = next_frame_target - this_frame
                if delay > 0:
                    await asyncio.sleep(delay)
                next_frame_target = this_frame + limit_frame_duration

            self._render_game()
            self.clock.tick()

            events = loop.create_task(self.events())

            # Flip to show new frame
            await loop.run_in_executor(None, pg.display.flip)
            # don’t want to accidentally start drawing again until events are done
            await events

        pg.quit()
