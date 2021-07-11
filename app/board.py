import numpy as np
import jsons

ROW_COUNT = 6
COLUMN_COUNT = 9

class Board:

    def __init__(self):
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))

    def is_valid_move(self, col):
        return self.board[ROW_COUNT - 1][col] == 0

    def get_next_valid_row(self, col):
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def drop_disc(self, row, col, token):
        self.board[row][col] = token

    def display_current_board_state(self):
        print(np.flip(self.board, 0))

    def get_board(self):
        return self.board

    def board_as_serialized(self):
        return jsons.dump(self.board)
