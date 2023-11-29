import os

from views.player_view import PlayerView
from models.player import Player
from models.data import DataManager
from controllers.main_controller import MainController

class PlayerController:

    @staticmethod
    def create_player():
        player_infos = PlayerView.display_player_creation()
        try:
            player = Player(first_name=player_infos[0],
                        last_name=player_infos[1],
                        birthdate=player_infos[2])
            player._validate_birthdate(date_str=player_infos[2])
            save_player = DataManager(path="./data/players.json")
            save_player.save_data(player.to_dict())            
        except ValueError as e :
            print(f"Erreur {e}")
            MainController.menu_controller()