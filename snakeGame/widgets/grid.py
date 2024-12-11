import pygame as pg

from snakeGame.widgets.widget import Widget


class Grid(Widget):
    def __init__(self, x, y, width: int, height: int, num_rows: int, num_cols: int, line_width: int = 1,
                 line_color: pg.Color = pg.Color("white"), bg_color: pg.Color = pg.Color("black")):
        super().__init__(x, y, width, height)
        self.width = width
        self.height = height
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.line_width = line_width
        self.line_color = line_color
        self.bg_color = bg_color

        self.cell_height = (height - (num_rows + 1) * line_width) / num_rows
        self.cell_width = (width - (num_cols + 1) * line_width) / num_cols

        self.grid: list[list[int]] = [[]]

        self._populate_grid()

        self.print_grid()

        self.bg()
        self.lines()

    def update(self, screen: pg.Surface):
        # self.clear_elements()
        # self.bg()
        # self.lines()
        return

    def bg(self):
        bg = Widget(0, 0, self.width, self.height, (100, 100, 100))

    def lines(self):
        # Vertical lines
        for col in range(self.num_cols + 1):
            dx = col * (self.cell_width + self.line_width)
            line = Widget(dx, 0, self.line_width, self.height, self.line_color)
            self.add_element(line)

        # Horizontal lines
        for row in range(self.num_rows + 1):
            dy = row * (self.cell_height + self.line_width)
            line = Widget(0, dy, self.width, self.line_width, self.line_color)
            self.add_element(line)

        # up = Widget(0, 0, self.width, self.line_width, self.line_color)
        # down = Widget(0, self.height - self.line_width, self.width, self.line_width, self.line_color)
        # left = Widget(0, 0, self.line_width, self.height, self.line_color)
        # right = Widget(self.width - self.line_width, 0, self.line_width, self.height, self.line_color)
        #
        # self.add_element(up)
        # self.add_element(down)
        # self.add_element(left)
        # self.add_element(right)

    def get_cell_pos(self, row: int, col: int):
        """
        Get the position of the cell in the grid given the row and column.
        x = col * (cell_width + line_width)
        :param row:
        :param col:
        :return:
        """
        x = col * (self.cell_width + self.line_width) + self.line_width
        y = row * (self.cell_height + self.line_width) + self.line_width
        return x, y

    def get_cell_spacing(self):
        return self.cell_width, self.cell_height

    def _populate_grid(self):
        self.grid = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]

    def print_grid(self):
        """
        Debug method to print the grid
        :return:
        """
        for row in self.grid:
            print(row)
