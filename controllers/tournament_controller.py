import datetime
from models.tournament import Tournament
from models.data import DataManager
from controllers.main_controller import MainController
from views.tournament_view import TournamentView
from views.main_view import MenuView
from models.player import Player
from controllers.player_controller import PlayerController

class TournamentController:

    """Handles tournament creation"""
    @staticmethod
    def create_tournament():    

        tournament_info = TournamentView.display_tournament_creation()

        try:
            defines_start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            tournament = Tournament(name=tournament_info[0], 
                                    place=tournament_info[1], 
                                    start_date=defines_start_date,
                                    end_date=None,
                                    rounds=[],
                                    registered_players=[],
                                    notes=tournament_info[4],
                                    number_of_players=tournament_info[2], 
                                    number_of_rounds=tournament_info[3])
            
            players_infos = DataManager(path="./data/players.json")
            check_players = players_infos.load_data_set()
            
            tournament_infos = DataManager(path="./data/tournaments.json")
            tournaments = tournament_infos.load_data_set()
            
            PlayerController.register_a_player(tournament, check_players, tournaments)
                                
            tournament_infos.save_data(tournament.to_dict())
       

        except ValueError as e :
            print(f"Erreur {e}")
            MainController.menu_controller()
            return None
        return tournament
    



            
