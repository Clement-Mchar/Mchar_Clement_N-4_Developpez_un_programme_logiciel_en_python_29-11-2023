from rich.console import Console
from rich.table import Table
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

            except ValueError as e:
                print(f"Erreur {e}")

    @staticmethod
    def players_report():
        players_path = DataManager('./data/players.json')
        players = players_path.load_data_set()
        sorted_players = sorted(
            players, key=lambda x: (
                x["first_name"].lower(), x["last_name"].lower()
            )
        )

        table = Table(show_header=True, header_style="cyan")
        table.add_column("ID", style="white", justify="right")
        table.add_column("Prénom", style="white")
        table.add_column("Nom", style="white")
        table.add_column("Date de naissance", style="white")

        for player in sorted_players:
            table.add_row(
                str(player["id"]),
                player["first_name"],
                player["last_name"],
                player["birthdate"]
            )

        console = Console()
        console.print(table)
