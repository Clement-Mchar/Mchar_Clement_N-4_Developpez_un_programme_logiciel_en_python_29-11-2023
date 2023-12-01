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
        existing_tournaments = DataManager(path="./data/tournaments.json")
        tournaments = existing_tournaments.load_data_set()


        try:
            tournament_number = len(tournaments) + 1
            defines_start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            tournament = Tournament(number=tournament_number,
                                    name=tournament_info[0], 
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
            
           
            existing_tournaments.save_data(tournament.to_dict())
            
            PlayerController.register_a_player(tournament, check_players, tournaments)

            
                                
            
       

        except ValueError as e :
            print(f"Erreur {e}")
            MainController.menu_controller()
            return None
        return tournaments, tournament
    



            
