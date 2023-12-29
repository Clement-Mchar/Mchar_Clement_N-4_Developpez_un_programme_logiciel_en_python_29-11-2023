
from models.data import DataManager
from views.reports_view import ReportsView



class ReportController:

    @staticmethod
    def reports_menu():
        while True:
            try:
                choice = ReportsView.display_reports_menu()
                if choice == 1:
                    ReportController.players_report()
                if choice == 2:
                    ReportController.tournaments_report()
                if choice == 3:
                    ReportController.selected_tournament()
                if choice == 4:
                    ReportController.tournament_players()
                if choice == 5:
                    ReportController.tournament_rounds_and_matches()

            except ValueError as e:
                print(f"Erreur {e}")

    @staticmethod
    def players_report(program_state):
        players = program_state.players
        sorted_players = sorted(
            players, key=lambda x: (
                x["first_name"].lower(), x["last_name"].lower()
            )
        )
        ReportsView.display_players_report(sorted_players)

    def tournaments_report(program_state):
        tournaments = program_state.tournaments

        ReportsView.display_tournaments_report(tournaments)

    def selected_tournament(program_state):
        tournaments = program_state.tournaments
        ReportsView.display_selected_tournament(tournaments)

    def tournament_players(program_state):
        tournaments = program_state.tournaments
        players = program_state.players
        ReportsView.display_tournament_players(tournaments, players)

    def tournament_rounds_and_matches(program_state):
        tournaments = program_state.tournaments
        rounds = program_state.rounds
        matches = program_state.matches
        ReportsView.display_rounds_and_matches(tournaments, rounds, matches)
