from rich.console import Console

class RoundView:

    @classmethod
    def display_round_view(cls, new_round, displayed_matches):
        console = Console()
        console.print(f"[bold]Round N°{new_round.number} :[/bold]")

        for displayed_match in displayed_matches:
            match_row = f"{displayed_match[0]} {displayed_match[1]} contre {displayed_match[2]}"
            console.print(match_row)
        input("Appuyez sur entrée pour voir les résultats.")
    
    @classmethod
    def display_results(cls, matches):
        console = Console()

        for match in matches :
            match_row = f"{match.result}"
            console.print(match_row)