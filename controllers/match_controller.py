import random
from models.match import Match
from views.round_view import RoundView
from views.match_view import MatchView
from models.data import DataManager


class MatchController:

    match_counter = 0

    @staticmethod
    def create_match(rounds, new_round, players_list, players_scores):
        matches_path = DataManager("./data/matches.json")
        matches = matches_path.load_data_set()
        played_players = []
        round_matches = []

        match_players = zip(players_list[::2], players_list[1::2])

        match_id = len(matches) + 1

        for match_id, (
            player_1,
            player_2
        ) in enumerate(match_players, start=1):

            while (player_1[0], player_2[0]) in played_players:
                random.shuffle(players_list)
                player_1, player_2 = players_list[0], players_list[1]


            match = Match(
                id=match_id,
                round_id=new_round.id,
                name=f"Match N.{match_id}",
                player_1=player_1,
                player_2=player_2,
                result=""
            )

            played_players.append((player_1[0], player_2[0]))
            
            round_matches.append(match)

            DataManager.update_rounds(rounds)
        MatchController.save_match_tuple(new_round, rounds, round_matches, matches_path, players_scores)

    def save_match_tuple(new_round, rounds, round_matches, matches_path, players_scores):
        
        RoundView.display_round_view(new_round, round_matches)
        for match in round_matches:
            MatchController.handle_match_result(match, players_scores)
            match_tuple = (
                [
                    match.player_1[1],
                    match.player_1[2]
                ],
                [
                    match.player_2[1],
                    match.player_2[2]
                ]
            )
            matches_path.save_data(match.to_dict())
            new_round.matches.append(match_tuple)
            DataManager.update_rounds(rounds)
        

    @staticmethod
    def handle_match_result(match, players_scores ):

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
                    match.player_1[2] = 1
                    match.player_2[2] = 0
                elif player_1_result == 0.5:
                    match.player_1[2] = 0.5
                    match.player_2[2] = 0.5
                elif player_1_result == 0:
                    match.player_1[2] = 0
                    match.player_2[2] = 1

                for player in players_scores :
                    if match.player_1[0] == player[0]:
                        player[2] += match.player_1[2]
                    elif match.player_2[0] == player[0]:
                        player[2] += match.player_2[2]
                
                match.result = f"{match.player_1[2]}-{match.player_2[2]}"

                break

            except ValueError as e:
                print(f"Erreur: {e}")
                print("Veuillez entrer un score valide (0, 0.5, ou 1).")
