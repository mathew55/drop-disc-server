from flask import Blueprint
from flask import request
from app.services.move_manager import next_board_move
from app.services.move_manager import next_player
from app.model.game_models.player import Player
from app.model.response_models.response import Response
from app.context.app_context import ApplicationContext
from app.services.player_manager import PlayerMatcher
from app.context.conf import Config


config = Config()
baseEndpoint = config.get_config_value("endpoint", "base")
game_controller = Blueprint('game_controller', __name__, template_folder="templates")


cx = ApplicationContext.getContext()
conn = PlayerMatcher()


#TODO Add validation to check if the request is of application/json type

@game_controller.route(f'{baseEndpoint}/startgame/', methods= ["POST"])
def start_game():
    player_name = request.args.get("player_name")
    player_token = int(request.args.get("player_token"))
    player = Player(player_name, player_token)
    cx.log.info(f"Request from Player - {player} to start a game, Adding player to player pool")
    conn.add_player_to_pool(player)
    game = conn.start_match()
    cx.log.info(f"Game started Successfully, Initial Game State- {game}")
    return Response(
        payload=game.game_state_as_dict(),
        message=f"Opponent Found, Starting the Game",
        code=200
    ).response()


@game_controller.route(f'{baseEndpoint}/nextmove/', methods= ["POST"])
def make_move():
    game_id = request.args.get("game_id")
    move_col = int(request.args.get("move_col"))

    cx.log.info(f"Request Received to put disc in the column - {move_col}")
    game = next_board_move(game_id, move_col)

    return Response(
        payload=game.game_state_as_dict(),
        message=f"Successfully made the move, The current game state attached in payload",
        code=200
    ).response()


@game_controller.route(f'{baseEndpoint}/getgamestate/', methods= ["POST"])
def get_game_state():
    game_id = request.args.get("game_id")
    cx.log.info(f"Request received to fetch game state of  {game_id}")
    game = next_player(game_id)
    cx.log.info(f"Game State Retrieved Suceesfully, Gamestate - {game.game_state_as_dict()}")
    return Response(
        payload=game.game_state_as_dict(),
        message=f"Returning current game state",
        code=200
    ).response()
