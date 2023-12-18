from rich.console import Console
from rich.table import Table

class TournamentView:

    @classmethod
    def display_tournament_creation(cls):

        tournament_name = input("Nom du tournoi : ")
        tournament_place = input("Lieu du tournoi : ")
        tournament_players = input("Nombre de joueurs : ")
        tournament_rounds = input("Nombre de rounds : ")
        tournament_description = input("Description : ")

        return [
                tournament_name,
                tournament_place,
                int(tournament_players),
                int(tournament_rounds),
                tournament_description
                ]

    @classmethod
    def display_players_registration(cls, existing_players):

        print(existing_players)

        player_id = int(input("Entrez l'id du joueur à inscrire au tournoi: "))

        return player_id
    
    @classmethod
    def display_tournament_ranking(players_list):
        
        console.print("Voici le classement du tournoi :")
        
        table = Table(show_header=True, header_style="cyan")
        table.add_column("Place", style="white", justify="left")
        table.add_column("Prénom", style="white")
        table.add_column("Nom", style="white")
        table.add_column("Score", style="white")

        for rank, player in enumerate(players_list, start=1):
            table.add_row(
                str(rank),
                player[1],
                player[2],
                str(player[3])
            )
        console = Console()
        console.print(table)
