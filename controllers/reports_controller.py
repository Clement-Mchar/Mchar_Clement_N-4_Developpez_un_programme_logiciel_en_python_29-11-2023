from rich.console import Console
from rich.table import Table
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
                    ReportController.tournament_rounds(program_state)

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
        choice = ReportsView.display_selected_tournament(program_state)
        tournaments = program_state.tournaments
        console = Console()
        new_table = Table(show_header=True, header_style="cyan")

        while True:
            try:
                current_tournament = next(
                    tournament for tournament in tournaments
                    if tournament['id'] == int(choice)
                )

                new_table = Table(show_header=True, header_style="cyan")
                new_table.add_column(
                    "Nom du tournoi", style="white", justify="left"
                )

                new_table.add_column("Date de début", style="white")
                new_table.add_column("Date de fin", style="white")

                new_table.add_row(
                    current_tournament["name"],
                    current_tournament["start_date"],
                    current_tournament["end_date"]
                )
                console.print(new_table)
                break

            except StopIteration:
                print(
                    "Aucun tournoi trouvé avec cet ID. "
                    "Veuillez réessayer."
                )

    def tournament_players(program_state):
        choice = ReportsView.display_tournament_players(program_state)
        tournaments = program_state.tournaments
        players = program_state.players
        console = Console()
        new_table = Table(show_header=True, header_style="cyan")

        while True:
            try:
                current_tournament = next(
                    tournament for tournament in tournaments
                    if tournament['id'] == int(choice)
                )

                tournament_player_ids = current_tournament['players']
                tournament_players = [
                    player for player in players
                    if player['id'] in tournament_player_ids
                ]

                if not tournament_players:
                    raise StopIteration

                new_table = Table(show_header=True, header_style="cyan")
                new_table.add_column("ID", style="white", justify="right")
                new_table.add_column("Prénom", style="white")
                new_table.add_column("Nom", style="white")
                new_table.add_column("Date de Naissance", style="white")

                for player in tournament_players:
                    new_table.add_row(
                        str(player["id"]),
                        player["first_name"],
                        player["last_name"],
                        player["birthdate"]
                    )

                console.print(new_table)
                break
            except StopIteration:
                print("Aucun tournoi trouvé avec cet ID")

    def tournament_rounds(program_state):
        tournaments = program_state.tournaments
        rounds = program_state.rounds
        console = Console()

        while True:
            try:
                choice = ReportsView.display_rounds(program_state)
                current_tournament = next(
                    tournament for tournament in tournaments
                    if tournament['id'] == int(choice)
                )

                tournament_rounds = [
                    new_round for new_round in rounds
                    if new_round["tournament_id"] == current_tournament["id"]
                ]

                if not tournament_rounds:
                    raise StopIteration

                new_table = Table(show_header=True, header_style="cyan")
                new_table.add_column("ID", style="white", justify="right")
                new_table.add_column("Nom", style="white")

                for one_round in tournament_rounds:
                    new_table.add_row(
                        str(one_round["id"]),
                        one_round["name"],
                    )

                console.print(new_table)
                break
            except StopIteration:
                print("Aucun round trouvé avec cet ID")

        ReportController.round_matches(program_state)

    def round_matches(program_state):
        rounds = program_state.rounds
        matches = program_state.matches
        console = Console()

        while True:
            try:
                choice = ReportsView.display_matches(program_state)
                current_round = next(
                    round for round in rounds
                    if round['id'] == int(choice)
                )

                round_matches = [
                    match for match in matches
                    if match["round_id"] == current_round['id']
                ]

                if not round_matches:
                    raise StopIteration

                new_table = Table(show_header=True, header_style="cyan")
                new_table.add_column("ID", style="white", justify="right")
                new_table.add_column("Nom", style="white")
                new_table.add_column("Joueur 1", style="white")
                new_table.add_column("Joueur 2", style="white")
                new_table.add_column(
                    "Résultat", style="white", justify="center"
                )

                for match in round_matches:
                    print(match)
                    player_1_name = match["player_1"][1]
                    player_2_name = match["player_2"][1]
                    player_1_str = ''.join(map(str, player_1_name))
                    player_2_str = ''.join(map(str, player_2_name))
                    new_table.add_row(

                        str(match["id"]),
                        match["name"],
                        player_1_str,
                        player_2_str,
                        match["result"]
                    )

                console.print(new_table)

                break
            except StopIteration:
                print("Aucun round trouvé avec cet ID")
