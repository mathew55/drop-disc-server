import jsons

ROW_COUNT = 6
COLUMN_COUNT = 9

class Game_Logic:

    def check_victory(self, board, token):
        flag = False
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                print(f"1st Iteration - {board[r][c]}")
                if board[r][c] == token:
                    print("1st Condition satisfied")
                if board[r][c] == token and board[r][c + 1] == token and board[r][c + 2] == token and \
                        board[r][c + 3] == token and board[r][c + 4] == token:
                    flag = True

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == token and board[r + 1][c] == token and board[r + 2][c] == token and \
                        board[r + 3][c] == token and board[r + 4][c] == token:
                    flag = True

        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == token and board[r + 1][c + 1] == token and board[r + 2][c + 2] == token and \
                        board[r + 3][c + 3] == token:
                    flag = True

        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == token and board[r - 1][c + 1] == token and board[r - 2][c + 2] == token and \
                        board[r - 3][c + 3] == token:
                    flag = True

        print(f"Winner Flag - {flag}")
        return flag