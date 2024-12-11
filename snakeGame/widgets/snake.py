"""
This module contains the Snake class which is a subclass of AnimatedEntity
The Snake class is used to represent the snake in the game

The Snake class is responsible for:
- Moving the snake
- Growing the snake
- Handling boundary collision
- Handling user input

Bug:
- Idk why but direction is reversed instead of [x, y] it is [y, x]
"""
import pygame as pg
import sys

from PIL.ImageChops import screen

from snakeGame.widgets.widget import Widget
from snakeGame.widgets.grid import Grid


class Snake(Widget):
    def __init__(self, grid: Grid, initial_pos: pg.Vector2 = [0, 0], initial_length: int = 3,
                 color: pg.Color = pg.Color("green")):
        super().__init__(grid.x, grid.y, grid.width, grid.height)
        self.grid = grid
        self.color = color
        self.direction = [1, 0]  # Start moving to the right
        self.speed = 1
        self.body = [[0, 1], [0, 0]]
        self.segments: list[Widget] = []
        self.grow = False
        self.last_time = pg.time.get_ticks()

        print(self.body)

        self.load_body()

    def update(self, screen: pg.Surface):
        # Calculate new head position
        if pg.time.get_ticks() - self.last_time < 1000 / self.speed:
            return
        self.last_time = pg.time.get_ticks()

        for i in range(1, len(self.body)):
            pg.draw.rect(self.grid.surface, (255, 100, 200), self.segments[i].rect)
            screen.blit(self.grid.surface, self.grid.rect.topleft)

        if not self.grow:
            self.move_snake()
        else:
            self.grow_snake()

        # Handle boundary collision
        self.handle_boundary_collision()

    def move_snake(self):
        """
        Manipulating the list of segments to simulate snake movement
        We always start iterating the body and move the head to the new position
        :return:
        """
        if self.check_invalid_move():
            print("Invalid move detected")
            return

        # First we move the body to the previous positions
        for i in range(1, len(self.body)):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y
            self.body[i] = self.body[i - 1]

        # Then we move the head
        self.body[0][0] += self.direction[1]
        self.body[0][1] += self.direction[0]

        new_pos = self.grid.get_cell_pos(self.body[0][0], self.body[0][1])
        print("Head at: ", self.body[0], "New pos: ", new_pos)

        self.segments[0].x = new_pos[0]
        self.segments[0].y = new_pos[1]

        print("Len of elements: ", len(self._elements))

    def check_invalid_move(self):
        if self.body[0][0] + self.direction[1] < 0 or self.body[0][0] + self.direction[1] >= self.grid.num_cols:
            return True
        if self.body[0][1] + self.direction[0] < 0 or self.body[0][1] + self.direction[0] >= self.grid.num_rows:
            return True
        return False

    def load_body(self):
        for section in self.body:
            x, y = self.grid.get_cell_pos(section[0], section[1])
            segment_element = Element(x, y, self.grid.get_cell_spacing()[0], self.grid.get_cell_spacing()[1], self.color)
            self.segments.append(segment_element)
            self.add_element(segment_element)
            print("Loading segment: ", section[0], section[1], "at: ", x, y)

    def change_direction(self, new_direction):
        if self.direction[0] + new_direction[0] == 0 and self.direction[1] + new_direction[1] == 0:
            print("Invalid direction change")
            return
        self.direction = new_direction

    def grow_snake(self):
        """
        Moves the snake as normal but we add a new segment at the end
        :return:
        """
        last_seg_pos = [self.segments[-1].x, self.segments[-1].y]
        last_body_pos = self.body[-1]

        self.move_snake()

        self.segments.append(Element(last_seg_pos[0], last_seg_pos[1], self.grid.cell_width, self.grid.cell_height, self.color))
        self.body.append(last_body_pos)

        self.grow = False

    def handle_boundary_collision(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= self.grid.num_cols or head_y < 0 or head_y >= self.grid.num_rows:
            print("Collision with boundary detected!")

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.change_direction([0, -1])
            elif event.key == pg.K_DOWN:
                self.change_direction([0, 1])
            elif event.key == pg.K_LEFT:
                self.change_direction([-1, 0])
            elif event.key == pg.K_RIGHT:
                self.change_direction([1, 0])
            elif event.key == pg.K_SPACE:
                print("Growing snake")
                self.grow_snake()
            elif event.key == pg.K_ESCAPE:
                print("Exiting game")
                pg.quit()
                sys.exit()

            print("Event key: ", event.key)
