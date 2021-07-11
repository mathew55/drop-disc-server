from flask import Blueprint
from app.connection_manager import Connections
import json
from app.move import next_board_move
from app.move import next_player
from app.player import Player
from flask import request

game_controller = Blueprint('game_controller', __name__, template_folder="templates")
connection_pool = Connections()

@game_controller.route('/start-game/', methods= ["POST"])
def start_game():
    player_name = request.args.get("player_name")
    print(f"Welcome to the game {player_name}")
    player = Player(player_name, 1)
    print(f"Player - {player}")
    connection_pool.add_player_to_connection_queue(player)
    game = connection_pool.start_match()
    print(f"Game started - {game}")
    return f"{json.dumps(game.to_ser_obj())}"


@game_controller.route('/next-move/', methods= ["POST"])
def make_move():
    game_id = 1
    move_col = int(request.args.get("move_col"))
    game = next_board_move(game_id, move_col)
    return f"{json.dumps(game)}"

@game_controller.route('/get-player/', methods= ["POST"])
def current_player():
    game_id = 1
    game = next_player(1)
    return f"{json.dumps(game.to_ser_obj())}"
