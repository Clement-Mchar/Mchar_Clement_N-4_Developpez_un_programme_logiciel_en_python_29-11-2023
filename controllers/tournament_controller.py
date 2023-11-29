import datetime
from models.tournament import Tournament
from models.data import DataManager
from controllers.main_controller import MainController
from views.tournament_view import TournamentView

class TournamentController:

    @staticmethod
    def create_tournament():
        
        """Handles tournament creation"""
        tournament_info = TournamentView.display_tournament_creation()

        try:
            tournament = Tournament(name=tournament_info[0], 
                                    place=tournament_info[1], 
                                    number_of_players=tournament_info[2], 
                                    number_of_rounds=tournament_info[3],
                                    start_date=None,
                                    end_date=None)
            save_tournament = DataManager(path="./data/tournaments.json")
            save_tournament.save_data(tournament.to_dict())
            
            start_date = datetime.datetime.now()
            tournament.start_date = start_date.strftime("%d/%m/%Y %H:%M")
        except ValueError as e :
            print(f"Erreur {e}")
            MainController.menu_controller()
