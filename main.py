from app.board import Board
from app.game import Game_Logic
from app.game import Game
from app.player import Player

board = Board()
game_logic = Game_Logic()
player1 = Player("Mathew", 1)
player2 = Player("Nisha", 2)
game = Game([player1, player2], board, game_logic)

while not game.game_over:
    next_turn_player =  game.get_next_turn_player()
    insert_position_user = int(input(f"It's your turn {next_turn_player.name}, Please enter a column (1 - 9):"))
    insert_position_np = insert_position_user - 1
    if game.board.is_valid_move(insert_position_np):
        row = game.board.get_next_valid_row(insert_position_np)
        board.drop_disc(row, insert_position_np, next_turn_player.token)
        if game_logic.check_victory(game.board.get_board(), next_turn_player.token):
            game.declare_winner(next_turn_player)

    board.display_current_board_state()
    game.next_turn()

print(f"Game Over - The Winner is {game.winner}")