import pygame as pg
import pygame.gfxdraw
import pygame.event
from snakeGame.widgets.widget import Widget

class RoundedButton(Widget):
    def __init__(self, screen, x, y, width, height, text, font_size, font_color, bg_color, border_color, border_width,
                 corner_radius=10, on_click: callable = lambda: None):

        # Validate corner radius
        if width <= 2 * corner_radius or height <= 2 * corner_radius:
            raise ValueError(
                f"Both height (self.rect.height) and width (self.rect.width) must be > 2 * corner radius ({corner_radius})")

        # Validate border width
        if border_width > corner_radius:
            raise ValueError(f"Border width ({border_width}) must be <= corner radius ({corner_radius})")

        super().__init__(screen, x, y, width, height)

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

    def draw(self):
        # need to use anti aliasing circle drawing routines to smooth the corners
        pygame.gfxdraw.aacircle(self.screen, self.rect.left + self.corner_radius, self.rect.top + self.corner_radius,
                                self.corner_radius, self.border_color)
        pygame.gfxdraw.aacircle(self.screen, self.rect.right - self.corner_radius - 1, self.rect.top + self.corner_radius,
                                self.corner_radius, self.border_color)
        pygame.gfxdraw.aacircle(self.screen, self.rect.left + self.corner_radius, self.rect.bottom - self.corner_radius - 1,
                                self.corner_radius,
                                self.border_color)
        pygame.gfxdraw.aacircle(self.screen, self.rect.right - self.corner_radius - 1, self.rect.bottom - self.corner_radius - 1, self.corner_radius,
                                self.border_color)

        # Outer corner circles
        pygame.gfxdraw.filled_circle(self.screen, self.rect.left + self.corner_radius, self.rect.top + self.corner_radius,
                                     self.corner_radius, self.border_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.right - self.corner_radius - 1, self.rect.top + self.corner_radius,
                                     self.corner_radius,
                                     self.border_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.left + self.corner_radius, self.rect.bottom - self.corner_radius - 1,
                                     self.corner_radius,
                                     self.border_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.right - self.corner_radius - 1, self.rect.bottom - self.corner_radius - 1,
                                     self.corner_radius, self.border_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.left + self.corner_radius, self.rect.top + self.corner_radius,
                                     self.corner_radius, self.border_color)

        # Inner corner circles
        inner_radius = self.corner_radius - self.border_width
        pygame.gfxdraw.filled_circle(self.screen, self.rect.left + self.corner_radius, self.rect.top + self.corner_radius,
                                     inner_radius, self.bg_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.right - self.corner_radius - 1,
                                     self.rect.top + self.corner_radius,
                                     inner_radius,
                                     self.bg_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.left + self.corner_radius,
                                     self.rect.bottom - self.corner_radius - 1,
                                     inner_radius,
                                     self.bg_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.right - self.corner_radius - 1,
                                     self.rect.bottom - self.corner_radius - 1,
                                     inner_radius, self.bg_color)
        pygame.gfxdraw.filled_circle(self.screen, self.rect.left + self.corner_radius, self.rect.top + self.corner_radius,
                                     inner_radius, self.bg_color)

        # Outer rects (border rects)
        rect_tmp = pygame.Rect(self.rect)

        rect_tmp.width -= 2 * self.corner_radius
        rect_tmp.center = self.rect.center
        pygame.draw.rect(self.screen, self.border_color, rect_tmp)

        rect_tmp.width = self.rect.width
        rect_tmp.height -= 2 * self.corner_radius
        rect_tmp.center = self.rect.center
        pygame.draw.rect(self.screen, self.border_color, rect_tmp)

        # Inner rects
        rect_tmp = pygame.Rect(self.rect)
        rect_tmp.width -= 2 * self.corner_radius
        rect_tmp.height -= 2 * self.border_width
        rect_tmp.center = self.rect.center
        pygame.draw.rect(self.screen, self.bg_color, rect_tmp)

        rect_tmp.width = self.rect.width - 2 * self.border_width
        rect_tmp.height -= self.rect.height - 2 * self.corner_radius
        rect_tmp.center = self.rect.center
        pygame.draw.rect(self.screen, self.bg_color, rect_tmp)

        # Render text
        text_surface = self.font.render(self.text, True, self.font_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        self.screen.blit(text_surface, text_rect)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pg.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos) and self.clicked:
                if self.on_click:
                    self.on_click()
            self.clicked = False
