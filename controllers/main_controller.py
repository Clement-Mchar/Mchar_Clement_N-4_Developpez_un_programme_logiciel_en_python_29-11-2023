from views.main_view import MenuView
from models.data import DataManager



class MainController:
    """Handles the menu
    Triggers all the other controllers"""
    program_state = None

    @staticmethod
    def set_program_state(program_state):
        MainController.program_state = program_state

    @staticmethod
    def menu_controller(program_state):
        from controllers.player_controller import PlayerController
        from controllers.tournament_controller import TournamentController
        from controllers.reports_controller import ReportController

        while True:
            if program_state.tournaments and program_state.tournaments[-1].get('is_over', True) is False:
                MainController.load_program_state(program_state)
            try:
                choice = MenuView.display_main_menu()
                if choice == 1:
                    PlayerController.create_player(program_state)
                elif choice == 2:
                    TournamentController.create_tournament(program_state)
                elif choice == 3:
                    ReportController.reports_menu()
                else:
                    print("Erreur : veuillez faire un choix valide.")
                    MenuView.display_main_menu()
            except ValueError as e:
                print(f"Erreur {e}")

    def load_program_state(program_state):
        from controllers.player_controller import PlayerController
        from controllers.round_controller import RoundController
        from controllers.match_controller import MatchController
        tournaments = program_state.tournaments
        program_state.current_tournament = tournaments[-1]
        tournament = program_state.current_tournament
        rounds = program_state.rounds
        program_state.current_round = rounds[-1]
        new_round = program_state.current_round


        while len(tournament['players']) < tournament['number_of_players']:
            MainController.load_registered_players(program_state)
            PlayerController.register_a_player(program_state)
        if len(tournament['rounds']) <= tournament['number_of_rounds']:
            if rounds:
                program_state.current_round = rounds[-1]
                MainController.load_registered_players(program_state)
                MainController.load_rounds(program_state)
                MainController.load_matches(program_state)
                RoundController.create_round(program_state)
            else:
                MainController.load_registered_players(program_state)
                RoundController.create_round(program_state)

    def load_registered_players(program_state):
        tournament = program_state.tournaments[-1]
        players = program_state.players
        registered_players = program_state.registered_players
        for registered_player in tournament['players']:
            registered_player = next(
                player for player in players
                if player['id'] == registered_player
            )
            name = f"{registered_player["first_name"]} {registered_player["last_name"]}"
            score = 0
            registered_players.append(
                [
                    registered_player["id"],
                    name,
                    score,
                ]
            )

    def load_rounds(program_state):
        
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
        from controllers.match_controller import MatchController
        matches = program_state.matches
        round_matches = program_state.round_matches
        tournament_round = program_state.current_round
        for match in matches:
            if match['round_id'] == tournament_round["id"]:
                round_matches.append(match)
            for match in round_matches:
                if not round_matches[0]['result']:
                    program_state.current_match = round_matches[0]
        MatchController.save_match(program_state)
        
        





                
    
