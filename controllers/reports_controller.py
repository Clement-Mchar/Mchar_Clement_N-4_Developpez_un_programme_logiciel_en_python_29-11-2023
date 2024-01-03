
from views.reports_view import ReportsView


class ReportController:
    """Handles reports display"""

    @staticmethod
    def reports_menu(program_state):
        """Handles reports menu"""
        while True:
            try:
                choice = ReportsView.display_reports_menu()
                if choice == 1:
                    ReportController.players_report(program_state)
                if choice == 2:
                    ReportController.tournaments_report(program_state)
                if choice == 3:
                    ReportController.selected_tournament(program_state)
                if choice == 4:
                    ReportController.tournament_players(program_state)
                if choice == 5:
                    ReportController.tournament_details(program_state)

            except ValueError as e:
                print(f"Erreur {e}")

    @staticmethod
    def players_report(program_state):
        players = program_state.players
        sorted_players = sorted(
            players, key=lambda x: (
                x["id"]
            )
        )
        ReportsView.display_players_report(sorted_players)

    def tournaments_report(program_state):
        ReportsView.display_tournaments_report(program_state)

    def selected_tournament(program_state):
        ReportsView.display_selected_tournament(program_state)

    def tournament_players(program_state):
        ReportsView.display_tournament_players(program_state)

    def tournament_details(program_state):
        ReportsView.display_rounds_and_matches(program_state)
