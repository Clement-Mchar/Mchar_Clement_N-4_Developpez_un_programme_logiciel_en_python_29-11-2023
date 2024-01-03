from rich.console import Console
from rich.table import Table


class TournamentView:

    @classmethod
    def display_tournament_creation(cls):

        console = Console()
        while True:
            try:
                tournament_name = input("Nom du tournoi : ")
                tournament_place = input("Lieu du tournoi : ")
                tournament_players = int(
                    console.input("Nombre de joueurs : ")
                )
                tournament_rounds = int(
                    console.input("Nombre de rounds : ")
                )
                tournament_description = input("Description : ")

                return [
                        tournament_name,
                        tournament_place,
                        tournament_players,
                        tournament_rounds,
                        tournament_description
                        ]

            except ValueError:
                print("Veuillez entrer un chiffre valide")

    @classmethod
    def display_players_registration(cls, existing_players):

        console = Console()
        console.print(existing_players)

        while True:
            try:
                player_id = int(
                    input("Entrez l'id du joueur à inscrire au tournoi: ")
                )
            except ValueError:
                print("veuillez entrer un id valide")
            return player_id

    @classmethod
    def display_tournament_ranking(cls, program_state):

        ranking = program_state.current_tournament['ranking']
        console = Console()
        console.print("Voici le classement du tournoi :")

        table = Table(show_header=True, header_style="cyan")
        table.add_column("Place", style="white", justify="left")
        table.add_column("Nom", style="white")
        table.add_column("Score", style="white")

        for rank, player in enumerate(ranking, start=1):
            table.add_row(
                str(rank),
                player[1],
                str(player[2])
            )

        console.print(table)
