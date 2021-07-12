from flask import Blueprint
import json
from app.move import next_board_move
from app.move import next_player
from app.player import Player
from flask import request
from app.model.response_models.response import Response
from app.context.app_context import ApplicationContext
from app.connection_manager import Connections


game_controller = Blueprint('game_controller', __name__, template_folder="templates")
cx = ApplicationContext.getContext()
conn = Connections()

@game_controller.route('/start-game/', methods= ["POST"])
def start_game():
    player_name = request.args.get("player_name")
    player_token = int(request.args.get("player_token"))
    player = Player(player_name, player_token)
    print(f"Request from Player - {player}")
    conn.add_player_to_pool(player)
    game = conn.start_match()
    print(f"Game started - {game}")
    return Response(
        payload=game.game_state_as_dict(),
        message=f"Opponent Found, Starting the Game",
        code=200
    ).response()

@game_controller.route('/next-move/', methods= ["POST"])
def make_move():
    game_id = request.args.get("game_id")
    move_col = int(request.args.get("move_col"))

    print(f"Move_COl - {move_col}")
    game = next_board_move(game_id, move_col)

    return Response(
        payload=game.game_state_as_dict(),
        message=f"Successfully made the move, The current game state attached in payload",
        code=200
    ).response()

@game_controller.route('/get-player/', methods= ["POST"])
def current_player():
    game_id = request.args.get("game_id")
    print(f"GameId is {game_id}")
    game = next_player(game_id)
    print(f"Game State is {game.game_state_as_dict()}")
    return Response(
        payload=game.game_state_as_dict(),
        message=f"Returning current game state",
        code=200
    ).response()
