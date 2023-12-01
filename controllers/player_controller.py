import os
import json
from views.player_view import PlayerView
from models.player import Player
from models.data import DataManager
from controllers.main_controller import MainController
from views.tournament_view import TournamentView
from views.main_view import MenuView

class PlayerController:
    """Handles players creation"""
    @staticmethod
    def create_player():

        player_infos = PlayerView.display_player_creation()
        players_infos = DataManager(path="./data/players.json")
        players = players_infos.load_data_set()
        player_number = len(players) + 1

        try:
            player = Player(number = player_number,
                        first_name=player_infos[0],
                        last_name=player_infos[1],
                        birthdate=player_infos[2])
            player._validate_birthdate(date_str=player_infos[2])
            save_player = DataManager(path="./data/players.json")
            save_player.save_data(player.to_dict())        
        
        except ValueError as e :
            print(f"Erreur {e}")
            MainController.menu_controller()
    
    """Handles players registering to the tournament"""
    @staticmethod
    def register_a_player(tournament, check_players, tournaments):
        
        if tournament:
            players_infos = DataManager(path="./data/players.json")
            check_players = players_infos.load_data_set()
            tournaments_infos = DataManager(path="./data/tournaments.json")
            tournaments = tournaments_infos.load_data_set()
            print(tournaments)
            for existing_tournament in tournaments:

                
                print(existing_tournament)
                existing_tournament_number = existing_tournament["number"]
        
                if existing_tournament_number == tournament.number:

                    for _ in range(existing_tournament["number_of_players"]) :
                        new_player_infos = TournamentView.display_players_registration()
                        first_name, last_name = new_player_infos
                        existing_player = next((player for player in check_players if
                                                 player["first_name"] == first_name and
                                                 player["last_name"] == last_name), None)

                        if existing_player:

                            player_found = True
                            
                            existing_tournament["registered_players"].append(f"{first_name} {last_name}")
                            

                            if player_found:
                                with open("./data/tournaments.json", "w", encoding="utf8") as json_file:
                                    json.dump(tournaments, json_file, indent=4, ensure_ascii=False)
                                print("Joueur inscrit avec succès.")
                                
                        else:
                            print("Ce joueur n'est pas enregistré.")
                            choice = input("Annuler la création du tournoi ? [o/n]")
                            

                            if choice.lower() == "o":
                                MenuView.display_main_menu()
                            else:
                                TournamentView.display_players_registration()
                                PlayerController.create_player()
                                break
