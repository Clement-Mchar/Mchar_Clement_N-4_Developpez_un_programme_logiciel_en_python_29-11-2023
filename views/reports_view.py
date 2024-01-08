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
            " et de tous les matchs du tour"
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
        choice = input("Veuillez entrer l'id du tournoi à afficher :")
        return choice

    def display_tournament_players(program_state):
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
        choice = input(
                "Veuillez entrer l'id du tournoi dont vous souhaitez "
                "afficher la liste de joueurs: "
            )

        return choice

    def display_rounds(program_state):
        tournaments = program_state.tournaments
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
        choice = input(
                "Veuillez entrer l'id du tournoi dont vous souhaitez "
                "afficher la liste des rounds: "
            )

        return choice

    def display_matches(program_state):
        choice = input(
                "Veuillez entrer l'id du round dont vous souhaitez "
                "afficher la liste des matches: "
        )
        return choice
