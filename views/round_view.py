from rich.console import Console

class RoundView:

    @classmethod
    def display_round_view(cls, new_round, matches):
        console = Console()
        console.print(f"[bold]Round N°{new_round.number} :[/bold]")
        for match in matches:
            match_row = f"{match['name']} {match['player_1']} contre {match['player_2']}"
            console.print(match_row)
        input("Appuyez sur entrée pour voir les résultats.")