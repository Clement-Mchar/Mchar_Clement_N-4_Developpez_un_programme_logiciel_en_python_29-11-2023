from rich.console import Console


class RoundView:

    @classmethod
    def display_round_view(cls, new_round, matches):

        console = Console()
        console.print(f"[bold]{new_round.name} :[/bold]")

        for match in matches:
            player_1_name = f"{match.player_1[1]} {match.player_1[2]}"
            player_2_name = f"{match.player_2[1]} {match.player_2[2]}"
            match_row = f"{match.name}: {player_1_name} contre {player_2_name}"
            console.print(match_row)
        console.input("Appuyez sur entrée pour commencer le round.")

    @classmethod
    def enter_match_result(cls, match):
        console = Console()
        player_1_name = f"{match.player_1[1]} {match.player_1[2]}"
        player_2_name = f"{match.player_2[1]} {match.player_2[2]}"
        console.print(f"{match.name}: {player_1_name} contre {player_2_name}")
        player_1_result = console.input(
            f"Entrez le résultat de {player_1_name}: "
        )
        player_2_result = console.input(
            f"Entrez le résultat de {player_2_name}: "
        )
        return player_1_result, player_2_result
