from models.match import Match
from models.data import DataManager
from views.round_view import RoundView
from views.match_view import MatchView


class MatchController:
    """Create all the round's matches."""

    @staticmethod
    def create_match(program_state):
        """Create a match and saves it to the matches.json file"""
        players_list = program_state.registered_players
        played_players = program_state.played_players
        rounds = program_state.rounds
        round_matches = program_state.round_matches
        current_round = program_state.current_round
        matches = program_state.matches
        matches_path = DataManager("./data/matches.json")

        match_players = zip(players_list[::2], players_list[1::2])

        available_matches = [
            (p1, p2) for p1 in players_list
            for p2 in players_list if p1 != p2
            and ((p1[0], p2[0]), (p2[0], p1[0]))
            not in played_players
        ]

        for match_id, (player_1, player_2) in enumerate(
            match_players, start=1
        ):

            if not available_matches:
                break
            match_id = len(matches) + 1
            match_number = len(program_state.round_matches) + 1
            match = Match(
                id=match_id,
                round_id=current_round["id"],
                name=f"Match N.{match_number}",
                player_1=player_1,
                player_2=player_2,
                result=None
            )

            played_players.append((player_1[0], player_2[0]))
            matches.append(match.to_dict())
            matches_path.save_data(match.to_dict())
            round_matches.append(match.to_dict())
            DataManager.update_rounds(rounds)

        RoundView.display_round_view(program_state)
        MatchController.save_match(program_state)

    def save_match(program_state):
        """Saves the match in the round's matches list"""
        rounds = program_state.rounds
        new_round = program_state.current_round
        round_matches = program_state.round_matches
        match = next(match for match in round_matches)
        for match in round_matches:
            program_state.current_match = match
            MatchController.handle_match_result(program_state)
            match_tuple = (
                [
                    match['player_1'][1],
                    match['player_1'][2]
                ],
                [
                    match['player_2'][1],
                    match['player_2'][2]
                ]
            )

            new_round['matches'].append(match_tuple)
            DataManager.update_rounds(rounds)
        round_matches = []
        program_state.round_matches = round_matches

    @staticmethod
    def handle_match_result(program_state):
        """Adds players's scores to their total score
        Updates tournament's ranking"""
        match = program_state.current_match
        ranking = program_state.current_tournament['ranking']

        while True:
            tournaments = program_state.tournaments
            match_result = MatchView.enter_match_result(program_state)
            player_1_result = match_result[0]
            player_2_result = match_result[1]
            player_1_result_float = float(player_1_result)
            player_2_result_float = float(player_2_result)
            only_results = [0, 0.5, 1]
            both_results = [player_1_result_float, player_2_result_float]

            try:
                if not all(
                    result in only_results for result in both_results
                ):
                    raise ValueError(
                        "Les résultats doivent être 0, 0.5, ou 1."
                    )

                player_1_result = (
                    int(player_1_result_float)
                    if player_1_result_float.is_integer()
                    else player_1_result_float
                )
                player_2_result = (
                    int(player_2_result_float)
                    if player_2_result_float.is_integer()
                    else player_2_result_float
                )

                if player_1_result == 1 and player_2_result != 0:
                    raise ValueError("Score invalide, veuillez rééssayer.")
                elif player_1_result == 0 and player_2_result != 1:
                    raise ValueError("Score invalide, veuillez rééssayer.")
                elif player_1_result == 0.5 and player_2_result != 0.5:
                    raise ValueError("Score invalide, veuillez rééssayer.")

                if player_1_result == 1:
                    match['player_1'][2] = 1
                    match['player_2'][2] = 0
                elif player_1_result == 0.5:
                    match['player_1'][2] = 0.5
                    match['player_2'][2] = 0.5
                elif player_1_result == 0:
                    match['player_1'][2] = 0
                    match['player_2'][2] = 1

                for player in ranking:
                    if match['player_1'][0] == player[0]:
                        player[2] += match['player_1'][2]
                    elif match['player_2'][0] == player[0]:
                        player[2] += match['player_2'][2]

                matches = program_state.matches
                written_match = next(
                    written_match for written_match in matches
                    if written_match["id"] == match["id"]
                )

                match['result'] = (
                    f"{match['player_1'][2]}-"
                    f"{match['player_2'][2]}"
                )

                written_match['result'] = (
                    f"{match['player_1'][2]}-"
                    f"{match['player_2'][2]}"
                )

                ranking = sorted(
                    ranking,
                    key=lambda x: (x[2]),
                    reverse=True
                )

                program_state.current_tournament['ranking'] = ranking
                DataManager.update_tournaments(tournaments)

                DataManager.update_matches(matches)
                break
            except ValueError as e:
                print(f"Erreur: {e}")
                print("Veuillez entrer un score valide (0, 0.5, ou 1).")
