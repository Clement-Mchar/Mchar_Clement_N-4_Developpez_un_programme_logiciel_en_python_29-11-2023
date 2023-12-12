from views.player_view import PlayerView
from models.player import Player
from models.data import DataManager
from controllers.main_controller import MainController
from views.tournament_view import TournamentView
from views.main_view import MenuView
from controllers.round_controller import RoundController


class PlayerController:

    """Handles players creation"""

    @staticmethod
    def create_player():

        player_infos = PlayerView.display_player_creation()
        players_infos = DataManager(path="./data/players.json")
        players = players_infos.load_data_set()

        try:
            player = Player(
                id=len(players) + 1,
                first_name=player_infos[0],
                last_name=player_infos[1],
                birthdate=player_infos[2]
            )
            player._validate_first_name(first_name=player_infos[0])
            player._validate_last_name(last_name=player_infos[1])
            player._validate_birthdate(date_str=player_infos[2])
            save_player = DataManager(path="./data/players.json")
            save_player.save_data(player.to_dict())

        except ValueError as e:
            print(f"Erreur: {e}")
            MainController.menu_controller()

    """Handles players registering to the tournament"""
    @staticmethod
    def register_a_player(tournaments, tournament
    ):  
        
        registered_players = []
        while len(tournament.players) < tournament.number_of_players:
            try:

                players_list = DataManager("./data/players.json")
                players =players_list.load_data_set()
                existing_players = []
                for player in players:

                    existing_players.append(
                        f"{player['id']}: {player['first_name']} "
                        f"{player['last_name']}"
                    )
                player_id = TournamentView.display_players_registration(
                    existing_players
                )

                existing_player = next(
                    (player for player in players if
                    player["id"] == player_id
                    ), None
                )
                if existing_player:
                    player_instance = Player(
                        id=player_id,
                        first_name=existing_player["first_name"],
                        last_name=existing_player["last_name"],
                        birthdate=existing_player["birthdate"]
                    )
                    player_instance.score = 0
                    tournament.players.append(f"{player_instance.id}")
                    registered_players.append([player_instance.first_name, player_instance.last_name, player_instance.score])
                    DataManager.update_tournaments(tournaments)
                    print("Joueur inscrit avec succès.")
                else:
                    print("Ce joueur n'est pas enregistré.")
                    choice = input(
                        "Annuler la création du tournoi ? [o/n]"
                    )
                    if choice.lower() == "o":
                        MenuView.display_main_menu()
            except ValueError as e:
                print(f"Erreur: {e}")
                MainController.menu_controller()
        RoundController.create_round(tournaments, tournament, registered_players)

