from app.context.app_context import ApplicationContext
from app.game import Game_Logic
from app.model.game_models.game import Game
from app.board import Board

board = Board()
game_logic = Game_Logic()
cx = ApplicationContext.getContext()

def next_board_move(game_id, move_col):
    game = cx.game_queue_map[game_id]
    next_turn_player = game.get_next_turn_player()
    insert_position_np = int(move_col)

    if game.board.is_valid_move(insert_position_np):
        row = game.board.get_next_valid_row(insert_position_np)
        game.board.drop_disc(row, insert_position_np, next_turn_player.token)
        if game.game_logic.check_victory(game.board.get_board(), next_turn_player.token):
            game.declare_winner(next_turn_player)

        game.next_turn()

    return game.game_state_as_dict()

def next_player(game_id):
    game = cx.game_queue_map[game_id]
    return game


