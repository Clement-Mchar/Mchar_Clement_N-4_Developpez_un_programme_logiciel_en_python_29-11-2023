import datetime
from models.tournament import Tournament
from models.data import DataManager
from controllers.main_controller import MainController
from views.tournament_view import TournamentView
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
            
            save_tournament = DataManager(path="./data/tournaments.json")
            save_tournament.save_data(tournament.to_dict())        

        except ValueError as e :
            print(f"Erreur {e}")
            MainController.menu_controller()
            return None
        
        TournamentController.register_a_player(tournament)
        return tournament
    


    @staticmethod
    def register_a_player(tournament):
            
        if tournament:
            registered_players = tournament.registered_players
            players_infos = DataManager(path="./data/players.json")
            check_players = list(players_infos.load_data_set())
            tournament_infos = DataManager(path="./data/tournaments.json")
            tournaments = list(tournament_infos.load_data_set())
            for _ in range(tournament.number_of_players) :
                new_player_infos = TournamentView.display_players_registration()
                first_name, last_name = new_player_infos
                existing_player = next((player for player in check_players if player["first_name"] == first_name and player["last_name"] == last_name), None)
                if existing_player:
                    tournament.get_registered_players().append(existing_player)
                    player_found = True
            for existing_tournament in tournaments:
                if existing_tournament["name"] == tournament.get_name():
                    existing_tournament["registered_players"] = registered_players
                    break

            if player_found:
                tournament_infos.save_data(tournaments)
                print("Joueur inscrit avec succès.")
            else:
                print("Ce joueur n'est pas enregistré.")

        TournamentView.display_players_registration()