from rich.console import Console


class MatchView:

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
