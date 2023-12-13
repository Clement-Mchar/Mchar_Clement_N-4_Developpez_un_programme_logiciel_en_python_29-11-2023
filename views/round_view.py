from rich.console import Console


class RoundView:

    @classmethod
    def display_round_view(cls, new_round, displayed_matches):
        console = Console()

        console.print(f"[bold]{new_round.name} :[/bold]")
        for displayed_match in displayed_matches:
            new_match = f"{displayed_match[1]} contre {displayed_match[2]}"
            match_row = f"{displayed_match[0]}: {new_match}"
            console.print(match_row)

    @classmethod
    def enter_match_result(cls, match):
        console = Console()

        player_1_name = f"{match.player_1[0]} {match.player_1[1]}"
        player_2_name = f"{match.player_2[0]} {match.player_2[1]}"
        player_1_result = console.input(
            f"Entrez le résultat de {player_1_name}: "
        )
        player_2_result = console.input(
            f"Entrez le résultat de {player_2_name}: "
        )
        return player_1_result, player_2_result
