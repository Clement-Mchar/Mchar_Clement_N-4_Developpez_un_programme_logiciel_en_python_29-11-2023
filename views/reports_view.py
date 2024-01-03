from rich.console import Console
from rich.table import Table


class ReportsView:

    """Display the report menu"""
    console = Console()

    @classmethod
    def display_reports_menu(cls):
        cls.console.print("Veuillez sélectionner le rapport à afficher :")
        cls.console.print("1: Afficher la liste des joueurs enregistrés")
        cls.console.print("2: Afficher la liste de tous les tournois")
        cls.console.print("3: Afficher les noms et dates d'un tournoi donné")
        cls.console.print(
            "4: Afficher la liste des joueurs du tournoi "
            "par ordre alphabétique"
        )
        cls.console.print(
            "5: Afficher la liste de tous les tours du tournoi"
            "et de tous les matchs du tour"
        )

        try:
            choice = input()
            return int(choice)
        except ValueError:
            print("Erreur: veuillez faire un choix valide")
            return cls.display_reports_menu()

    def display_players_report(sorted_players):
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

    def display_tournaments_report(program_state):
        tournaments = program_state.tournaments
        console = Console()
        table = Table(show_header=True, header_style="cyan")
        table.add_column("ID", style="white", justify="right")
        table.add_column("Nom", style="white")
        table.add_column("Lieu", style="white")
        table.add_column("Date de début", style="white")
        table.add_column("Date de fin", style="white")
        table.add_column("Nombre de joueurs", style="white", justify="right")
        table.add_column("Nombre de rounds", style="white", justify="right")
        table.add_column("Notes", style="white")
        table.add_column("Joueurs", style="white")
        table.add_column("Rounds", style="white")

        for tournament in tournaments:
            players_str = ', '.join(map(str, tournament["players"]))
            rounds_str = ', '.join(map(str, tournament["rounds"]))
            table.add_row(
                str(tournament["id"]),
                tournament["name"],
                tournament["place"],
                tournament["start_date"],
                tournament["end_date"],
                str(tournament["number_of_players"]),
                str(tournament["number_of_rounds"]),
                tournament["notes"],
                players_str,
                rounds_str
            )

        console.print(table)

    def display_selected_tournament(program_state):
        tournaments = program_state.tournaments
        console = Console()
        table = Table(show_header=True, header_style="cyan")
        table.add_column("ID", style="white", justify="right")
        table.add_column("Nom", style="white")
        table.add_column("Lieu", style="white")

        for tournament in tournaments:
            table.add_row(
                str(tournament["id"]),
                tournament["name"],
                tournament["place"]
            )
        console.print(table)

        while True:
            choice = input("Veuillez entrer l'id du tournoi à afficher :")

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

    def display_tournament_players(program_state):
        tournaments = program_state.tournaments
        players = program_state.players
        console = Console()
        table = Table(show_header=True, header_style="cyan")
        table.add_column("ID", style="white", justify="right")
        table.add_column("Nom", style="white")
        table.add_column("Lieu", style="white")

        for tournament in tournaments:
            table.add_row(
                str(tournament["id"]),
                tournament["name"],
                tournament["place"]
            )
        console.print(table)

        while True:
            choice = input(
                "Veuillez entrer l'id du tournoi dont vous souhaitez "
                "afficher la liste de joueurs: "
            )
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

    def display_rounds_and_matches(program_state):
        tournaments = program_state.tournaments
        rounds = program_state.rounds
        matches = program_state.matches
        console = Console()
        table = Table(show_header=True, header_style="cyan")
        table.add_column("ID", style="white", justify="right")
        table.add_column("Nom", style="white")
        table.add_column("Lieu", style="white")
        table.add_column("Rounds", style="white")

        for tournament in tournaments:
            rounds_str = ', '.join(map(str, tournament["rounds"]))
            table.add_row(
                str(tournament["id"]),
                tournament["name"],
                tournament["place"],
                rounds_str
            )
        console.print(table)

        while True:
            choice = input(
                "Veuillez entrer l'id du tournoi dont vous souhaitez "
                "afficher la liste des rounds: "
            )
            try:
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
                new_choice = input(
                    "Veuillez entrer l'id du round dont vous souhaitez "
                    "afficher la liste des matches: "
                )
                current_round = next(
                    round for round in rounds
                    if round['id'] == int(new_choice)
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
