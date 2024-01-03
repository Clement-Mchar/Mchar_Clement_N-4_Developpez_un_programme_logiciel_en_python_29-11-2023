from rich.console import Console


class MatchView:
    """Displays the match view"""

    @classmethod
    def enter_match_result(cls, program_state):
        match = program_state.current_match
        console = Console()
        while True:
            try:
                player_1_name = f"{match['player_1'][1]}"
                player_2_name = f"{match['player_2'][1]}"
                console.print(
                    (
                        f"{match['name']}: "
                        f"{player_1_name} contre {player_2_name}"
                    )
                )

                player_1_result = int(console.input(
                    f"Entrez le résultat de {player_1_name}: "
                    )
                )
                player_2_result = int(console.input(
                    f"Entrez le résultat de {player_2_name}: "
                ))
                return player_1_result, player_2_result
            except ValueError:
                print("Veuillez entrer un chiffre valide.")
