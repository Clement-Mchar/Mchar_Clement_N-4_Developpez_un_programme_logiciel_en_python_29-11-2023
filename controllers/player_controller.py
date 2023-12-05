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
        player_number = len(players) + 1

        try:
            player = Player(
                number=player_number,
                first_name=player_infos[0],
                last_name=player_infos[1],
                birthdate=player_infos[2]
            )

            player._validate_birthdate(date_str=player_infos[2])
            save_player = DataManager(path="./data/players.json")
            save_player.save_data(player.to_dict())

        except ValueError as e:
            print(f"Erreur {e}")
            MainController.menu_controller()

    """Handles players registering to the tournament"""
    @staticmethod
    def registered_players(players, rounds):

        tournaments_infos = DataManager(path="./data/tournaments.json")
        tournaments = tournaments_infos.load_data_set()
        tournament = tournaments[-1]

        if tournament:

            for existing_tournament in tournaments:
                existing_tournament_number = existing_tournament["number"]

                if existing_tournament_number == tournament["number"]:
                    PlayerController.register_a_player(
                        existing_tournament,
                        players,
                        tournaments,
                        rounds
                    )

    def register_a_player(
        existing_tournament,
        players,
        tournaments,
        rounds
    ):
        while True:
            for _ in range(existing_tournament["number_of_players"]):
                player_infos = TournamentView.display_players_registration()
                players_list = DataManager(path="./data/players.json")
                existing_players = players_list.load_data_set()
                first_name, last_name = player_infos
                existing_player = next((player for player in existing_players if
                                        player["first_name"] == first_name and
                                        player["last_name"] == last_name),
                                        None
                                    )

                if existing_player:
                    existing_tournament["players"].append(
                        f"{first_name} "
                        f"{last_name}"
                    )

                    player_instance = Player(
                        number=len(players) + 1,
                        first_name=first_name,
                        last_name=last_name,
                        birthdate=existing_player["birthdate"]
                    )

                    players.append(
                        f"{player_instance.first_name} "
                        f"{player_instance.last_name}"
                    )
                    DataManager.update_tournament(tournaments)
                    print("Joueur inscrit avec succès.")
                else:
                    print("Ce joueur n'est pas enregistré.")
                    choice = input(
                        "Annuler la création du tournoi ? [o/n]"
                    )

                    if choice.lower() == "o":
                        MenuView.display_main_menu()
            break
        RoundController.create_round(players, rounds)
