import pygame as pg

from snakeGame.widgets.widget import Widget


class ScoreBar(Widget):
    def __init__(self, x, y, width: int, height: int, font_size: int = 36):
        super().__init__(x, y, width, height)
        self.current_score = 0
        self.record_score = 0
        self.start_time = pg.time.get_ticks()
        self.font_size = font_size
        self.font = pg.font.Font(None, font_size)
        self.font_color = pg.Color("white")
        self.bg_color = pg.Color("black")
        self.record_color = pg.Color("yellow")

        self.time()
        self.score()
        self.record()

    def update_score(self, new_score):
        self.current_score = new_score
        if new_score > self.record_score:
            self.record_score = new_score

    def get_time(self):
        elapsed = self.get_elapsed_time()
        minutes = elapsed // 60000
        seconds = (elapsed % 60000) // 1000
        return f"{minutes:02}:{seconds:02}"

    def get_elapsed_time(self):
        return pg.time.get_ticks() - self.start_time

    def update(self, screen: pg.Surface):
        self.clear_elements()
        self.time()
        self.score()
        self.record()

    def time(self):
        time = Widget(0, (self.size[1] - self.font_size) // 2, self.size[0] // 3, self.size[1], self.bg_color)
        time_text = self.font.render(self.get_time(), True, self.font_color)
        time.surface.blit(time_text, (0, 0))
        self.add_element(time)

    def score(self):
        score = Widget(self.size[0] // 3, (self.size[1] - self.font_size) // 2, self.size[0] // 3, self.size[1], self.bg_color)
        score_text = self.font.render(f"Score: {self.current_score}", True, self.font_color)
        score.surface.blit(score_text, (0, 0))
        self.add_element(score)

    def record(self):
        record = Widget(self.size[0] * 2 // 3, (self.size[1] - self.font_size) // 2, self.size[0] // 3, self.size[1], self.bg_color)
        record_text = self.font.render(f"Record: {self.record_score}", True, self.record_color)
        record.surface.blit(record_text, (0, 0))
        self.add_element(record)
