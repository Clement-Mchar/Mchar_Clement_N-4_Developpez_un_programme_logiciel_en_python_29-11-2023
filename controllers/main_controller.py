from views.main_view import MenuView


class MainController:
    """Handles the program state
    Triggers all the other controllers."""
    program_state = None

    @staticmethod
    def set_program_state(program_state):
        MainController.program_state = program_state

    @staticmethod
    def menu_controller(program_state):
        """Handles the menu interactions."""
        from controllers.player_controller import PlayerController
        from controllers.tournament_controller import TournamentController
        from controllers.reports_controller import ReportController

        while True:
            tournaments = program_state.tournaments
            if tournaments and not tournaments[-1].get('is_over', True):
                """Checks if the last tournament is over"""
                MainController.load_program_state(program_state)
            try:
                choice = MenuView.display_main_menu()
                if choice == 1:
                    PlayerController.create_player(program_state)
                elif choice == 2:
                    TournamentController.create_tournament(program_state)
                elif choice == 3:
                    ReportController.reports_menu(program_state)
                else:
                    print("Erreur: veuillez faire un choix valide.")
                    MenuView.display_main_menu()
            except ValueError as e:
                print(f"Erreur: {e}")

    def load_program_state(program_state):
        """Loads program's previous state.
        Starts the program at the last saved step."""
        from controllers.player_controller import PlayerController
        from controllers.round_controller import RoundController
        from controllers.match_controller import MatchController

        tournaments = program_state.tournaments
        program_state.current_tournament = tournaments[-1]
        tournament = program_state.current_tournament
        rounds = program_state.rounds
        program_state.current_round = rounds[-1]

        while len(tournament['players']) < tournament['number_of_players']:
            MainController.load_registered_players(program_state)
            PlayerController.register_a_player(program_state)
        if len(tournament['rounds']) <= tournament['number_of_rounds']:
            if rounds:
                program_state.current_round = rounds[-1]
                MainController.load_registered_players(program_state)
                MainController.load_rounds(program_state)
                MainController.load_matches(program_state)
                round_matches = program_state.round_matches

                if round_matches:
                    for match in round_matches:
                        if match["result"] is None:
                            print(match)
                            program_state.current_match = match
                            MatchController.handle_match_result(program_state)
                RoundController.create_round(program_state)
            else:
                MainController.load_registered_players(program_state)
                RoundController.create_round(program_state)

    def load_registered_players(program_state):
        """Loads registered players from the current tournament."""
        tournament = program_state.tournaments[-1]
        players = program_state.players
        registered_players = program_state.registered_players
        for new_player in tournament['players']:
            new_player = next(
                player for player in players
                if player['id'] == new_player
            )
            name = f"{new_player["first_name"]} {new_player["last_name"]}"
            score = 0
            registered_players.append(
                [
                    new_player["id"],
                    name,
                    score,
                ]
            )

    def load_rounds(program_state):
        """Loads existing rounds from the current tournament
        Sets the current round."""
        tournament = program_state.tournaments[-1]
        rounds = program_state.rounds
        tournament_rounds = program_state.tournament_rounds
        for tournament_round in tournament['rounds']:
            tournament_round = next(
                new_round for new_round in rounds
                if new_round['id'] == tournament_round
            )
            tournament_rounds.append(tournament_round)
            program_state.current_round = tournament_round

    def load_matches(program_state):
        """Loads existing matches from the current round."""
        matches = program_state.matches
        round_matches = program_state.round_matches
        tournament_round = program_state.current_round
        for match in matches:
            if match['round_id'] == tournament_round["id"]:
                round_matches.append(match)
