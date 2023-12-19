import random
from models.match import Match
from views.round_view import RoundView
from views.match_view import MatchView
from models.data import DataManager


class MatchController:

    match_counter = 0

    @staticmethod
    def create_match(rounds, new_round, players_list):

        matches = []
        last_match_id = 0
        
        if len(rounds) >= 2 and rounds[-2]["matches"]:
            last_match_id = rounds[-2]["matches"][-1]
        else:
            last_match_id = 0
        
        match_number = len(matches) + 1

        played_players = []

        match_players = zip(players_list[::2], players_list[1::2])

        for match_number, (
            player_1,
            player_2
        ) in enumerate(match_players, start=1):

            while (player_1[0], player_2[0]) in played_players:
                random.shuffle(players_list)
                player_1, player_2 = players_list[0], players_list[1]

            match_id = last_match_id + match_number

            match = Match(
                id=match_id,
                round_id=new_round.id,
                name=f"Match N.{match_number}",
                player_1=player_1,
                player_2=player_2,
                result=""
            )

            played_players.append((player_1[0], player_2[0]))

            new_round.matches.append(match.id)
            matches.append(match)

        DataManager.update_rounds(rounds)
        RoundView.display_round_view(new_round, matches)
        for match in matches:
            MatchController.handle_match_result(match)

    @staticmethod
    def handle_match_result(match):

        while True:
            match_result = MatchView.enter_match_result(match)
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
                    match.player_1[3] += 1
                elif player_1_result == 0.5:
                    match.player_1[3] += 0.5
                    match.player_2[3] += 0.5
                elif player_1_result == 0:
                    match.player_2[3] += 1

                break

            except ValueError as e:
                print(f"Erreur: {e}")
                print("Veuillez entrer un score valide (0, 0.5, ou 1).")
        MatchController.save_match_tuple(match)

    def save_match_tuple(match):
        player_1_name = f"{match.player_1[1]} {match.player_1[2]}"
        player_2_name = f"{match.player_2[1]} {match.player_2[2]}"
        matches = DataManager("./data/matches.json")

        match_tuple = (
            {
                "name": player_1_name,
                "score": match.player_1[3]
            },
            {
                "name": player_2_name,
                "score": match.player_2[3]
            }
        )

        matches.save_data(match_tuple)
