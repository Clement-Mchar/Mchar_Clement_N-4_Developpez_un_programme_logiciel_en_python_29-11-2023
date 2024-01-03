from rich.console import Console


class RoundView:
    """Displays round view"""

    @classmethod
    def display_round_view(cls, program_state):
        new_round = program_state.current_round
        console = Console()
        console.print(f"[bold]{new_round['name']} :[/bold]")

        for match in program_state.round_matches:
            player_1_name = f"{match['player_1'][1]}"
            player_2_name = f"{match['player_2'][1]}"
            match_row = (
                f"{match['name']}: "
                f"{player_1_name} contre {player_2_name}"
            )
            console.print(match_row)
        console.input("Appuyez sur entrée pour commencer le round.")
