from flask import Blueprint
import json
from app.move import next_board_move
# from app.move import start_match
from app.move import next_player
from app.player import Player
from flask import request
from app.model.response_models.response import Response
from app.context.app_context import ApplicationContext


game_controller = Blueprint('game_controller', __name__, template_folder="templates")
cx = ApplicationContext.getContext()

@game_controller.route('/start-game/', methods= ["POST"])
def start_game():
    player_name = request.args.get("player_name")
    player = Player(player_name, 1)
    print(f"Player - {player}")
    cx.player_pool.add_player_to_pool(player)
    game = cx.player_pool.start_match()
    print(f"Game started - {game}")
    print(f"Game started for player- {player_name}")
    return Response(
        payload=game.game_state_as_dict(),
        message=f"Opponent Found, Starting the Game",
        code=200
    ).response()

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