import datetime
import os
from models.tournament import Tournament
from models.data import DataManager
from controllers.match_controller import MatchController
from controllers.main_controller import MainController
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController


class TournamentController:

    """Handles tournament creation"""

    @staticmethod
    def create_tournament():
        tournaments_path = DataManager("./data/tournaments.json")
        tournaments = tournaments_path.load_data_set()
        tournament_info = TournamentView.display_tournament_creation()
        
        try:
            tournament_id = len(tournaments) + 1
            start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            tournament = Tournament(
                id=tournament_id,
                name=tournament_info[0],
                place=tournament_info[1],
                start_date=start_date,
                end_date=None,
                rounds=[],
                players=[],
                notes=tournament_info[4],
                number_of_players=tournament_info[2],
                number_of_rounds=tournament_info[3]
            )

            tournament._validate_name(name=tournament_info[0])
            tournament._validate_place(place=tournament_info[1])
            tournament._validate_number_of_players(number_of_players=tournament_info[2])
            tournament._validate_number_of_rounds(number_of_rounds=tournament_info[3])
            
            tournaments.append(tournament.to_dict())
            tournaments_path.save_data(tournament.to_dict())
                
        except ValueError as e:
            print(f"Erreur {e}")
            MainController.menu_controller()
        PlayerController.register_a_player(tournaments, tournament)

        DataManager.update_tournaments(tournaments)


        

