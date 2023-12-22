from rich.console import Console


class RoundView:

    @classmethod
    def display_round_view(cls, new_round, round_matches):

        console = Console()
        console.print(f"[bold]{new_round.name} :[/bold]")

        for match in round_matches:
            player_1_name = f"{match.player_1[1]}"
            player_2_name = f"{match.player_2[1]}"
            match_row = f"{match.name}: {player_1_name} contre {player_2_name}"
            console.print(match_row)
        console.input("Appuyez sur entrée pour commencer le round.")
