from rich.console import Console
from rich.table import Table

class ReportsView:
    """Display the main menu"""

    console = Console()

    @classmethod
    def display_reports_menu(cls):
        cls.console.print("Veuillez sélectionner le rapport à afficher :")
        cls.console.print("1: Afficher la liste des joueurs enregistrés")
        cls.console.print("2: Afficher la liste de tous les tournois")
        cls.console.print("3: Afficher les noms et dates d'un tournoi donné")
        cls.console.print("4: Afficher la liste des joueurs du tournoi par ordre alphabétique")
        cls.console.print("5: Afficher la liste de tous les tours du tournoi et de tous les matchs du tour")

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
    
    def display_tournaments_report(tournaments):
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
    
    def display_selected_tournament(tournaments):
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
                current_tournament = next(tournament for tournament in tournaments if tournament['id'] == int(choice))
                new_table = Table(show_header=True, header_style="cyan")
                new_table.add_column("Nom du tournoi", style="white", justify="left")
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
                print("Aucun tournoi trouvé avec cet ID. Veuillez réessayer.")

    def display_tournament_players(tournaments, players):
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
                "afficher la liste de joueurs:"
            )
            try:
                current_tournament = next(tournament for tournament in tournaments if tournament['id'] == int(choice))

                tournament_player_ids = current_tournament['players']
                tournament_players = [player for player in players if player['id'] in tournament_player_ids]

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
