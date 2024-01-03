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
    def create_player(program_state):

        player_infos = PlayerView.display_player_creation()
        players = program_state.players
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
            PlayerView.display_player_creation()

    """Handles players registering to the tournament"""
    @staticmethod
    def register_a_player(
        program_state
    ):
        tournaments = program_state.tournaments
        tournament = program_state.current_tournament
        registered_players = program_state.registered_players
        ranking = tournament['ranking']
        while len(tournament['players']) < tournament['number_of_players']:
            try:
                players = program_state.players
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
                    (
                        player for player in players if
                        player["id"] == player_id
                    ),
                    None
                )
                if existing_player:
                    if int(player_id) not in tournament['players']:
                        new_player = Player(
                            id=int(player_id),
                            first_name=existing_player["first_name"],
                            last_name=existing_player["last_name"],
                            birthdate=existing_player["birthdate"]
                        )
                        new_player.score = 0
                        tournament['players'].append(new_player.id)
                        name = (
                            f"{new_player.first_name} "
                            f"{new_player._last_name}"
                        )

                        registered_players.append(
                            [
                                new_player.id,
                                name,
                                new_player.score,
                            ]
                        )
                        ranking.append(
                            [
                                new_player.id,
                                name,
                                new_player.score,
                            ]
                        )
                        DataManager.update_tournaments(tournaments)
                        print("Joueur inscrit avec succès.")
                    else:
                        print("Ce joueur est déjà inscrit, rééssayez.")

                else:
                    print("Ce joueur n'est pas enregistré.")
                    choice = input(
                        "Annuler la création du tournoi ? [o/n]"
                    )
                    if choice.lower() == "o":
                        MenuView.display_main_menu()
            except ValueError as e:
                print(f"Erreur: {e}")
                MainController.menu_controller(program_state)
        RoundController.create_round(program_state)
