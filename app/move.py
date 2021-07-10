from flask import Flask
from app.connection_manager import Connections
from app.board import Board
import jsons
from app.game import game_queue
import json


def next_board_move(game_id, move_col):
    game = game_queue[0]
    next_turn_player = game.get_next_turn_player()
    insert_position_np = int(move_col)

    if game.board.is_valid_move(insert_position_np):
        row = game.board.get_next_valid_row(insert_position_np)
        game.board.drop_disc(row, insert_position_np, next_turn_player.token)
        if game.game_logic.check_victory(game.board.get_board(), next_turn_player.token):
            game.declare_winner(next_turn_player)

    return game.to_ser_obj()

