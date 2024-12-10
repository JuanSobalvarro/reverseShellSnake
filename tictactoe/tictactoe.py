import pygame as pg
import sys

class TicTacToe:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((300, 300))
        pg.display.set_caption("Tic Tac Toe")
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = "X"
        self.font = pg.font.Font(None, 74)
        self.running = True

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        for row in range(1, 3):
            pg.draw.line(self.screen, (0, 0, 0), (0, 100 * row), (300, 100 * row), 2)
            pg.draw.line(self.screen, (0, 0, 0), (100 * row, 0), (100 * row, 300), 2)

    def draw_marks(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is not None:
                    mark = self.font.render(self.board[row][col], True, (0, 0, 0))
                    self.screen.blit(mark, (col * 100 + 30, row * 100 + 20))

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        return None

    def check_draw(self):
        for row in self.board:
            if None in row:
                return False
        return True

    def handle_click(self, pos):
        row, col = pos[1] // 100, pos[0] // 100
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            winner = self.check_winner()
            if winner:
                print(f"{winner} wins!")
                self.running = False
            elif self.check_draw():
                print("Draw!")
                self.running = False
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.handle_click(pg.mouse.get_pos())
            self.draw_board()
            self.draw_marks()
            pg.display.flip()