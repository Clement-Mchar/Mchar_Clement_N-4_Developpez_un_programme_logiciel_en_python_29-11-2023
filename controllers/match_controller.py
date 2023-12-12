import random
from models.match import Match
from views.round_view import RoundView
from models.data import DataManager

class MatchController :

    @staticmethod
    def create_match(rounds, new_round, players_list):
        matches_path = DataManager("./data/matches.json")
        matches = matches_path.load_data_set()

        displayed_matches = []
        match_players = zip(players_list[::2], players_list[1::2])
        match_number = len(displayed_matches) +1
        
        for match_number, (
            player_1, 
            player_2
        ) in enumerate(match_players, start=1):
            match = Match(
                id=new_round.id,
                name=f"Match N.{match_number}:",
                player_1=player_1,
                player_2=player_2,
                result=""
            )
            displayed_player_1 = f"{player_1[0]} {player_1[1]}"
            displayed_player_2 = f"{player_2[0]} {player_2[1]}"
            match_tuple =({
                "name": displayed_player_1,
                "score": player_1[2]
            },
            {   
                "name":displayed_player_2,
                "score": player_2[2]
            })

            displayed_match = [
                match.name,
                displayed_player_1,
                displayed_player_2
            ]

            displayed_matches.append(displayed_match)
            RoundView.display_round_view(new_round, [displayed_match])
        
            new_round.matches.append(match.to_dict())

            MatchController.handle_match_result(new_round, match, match_tuple)
            players_list = sorted(players_list, key=lambda x: (x[2]), reverse=True)
            print(players_list)

            


            matches_path.save_data(match_tuple)
        DataManager.update_rounds(rounds)

    @staticmethod
    def handle_match_result(new_round, match, match_tuple):
        while True:
            match_result = RoundView.enter_match_result(match)
            player_1_result = match_result[0]
            player_2_result = match_result[1]

            try:
                player_1_result_float = float(player_1_result)
                player_2_result_float = float(player_2_result)

                if player_1_result_float not in [0, 0.5, 1] or player_2_result_float not in [0, 0.5, 1]:
                    raise ValueError("Les résultats doivent être 0, 0.5, ou 1.")

                player_1_result = int(player_1_result_float) if player_1_result_float.is_integer() else player_1_result_float
                player_2_result = int(player_2_result_float) if player_2_result_float.is_integer() else player_2_result_float

                if player_1_result == 1 and player_2_result != 0:
                    raise ValueError("Si le joueur 1 gagne (score 1), le joueur 2 doit avoir un score de 0.")
                elif player_1_result == 0 and player_2_result != 1:
                    raise ValueError("Si le joueur 1 perd (score 0), le joueur 2 doit avoir un score de 1.")
                elif player_1_result == 0.5 and player_2_result != 0.5:
                    raise ValueError("Si le joueur 1 fait match nul (score 0.5), le joueur 2 doit aussi avoir un score de 0.5.")
                
                if player_1_result == 1:
                    new_round.matches[-1]['player_1'][2] += 1
                    match_tuple[0]['score'] += 1
                elif player_1_result == 0.5:
                    new_round.matches[-1]['player_1'][2] += 0.5
                    match_tuple[0]['score'] += 0.5
                    new_round.matches[-1]['player_2'][2] += 0.5
                    match_tuple[1]['score'] += 0.5
                elif player_1_result == 0:
                    new_round.matches[-1]['player_2'][2] += 1
                    match_tuple[1]['score'] += 1

                new_round.matches[-1]['result'] = f"{player_1_result}-{player_2_result}"

                break

            except ValueError as e:
                print(f"Erreur: {e}")
                print("Veuillez entrer un score valide (0, 0.5, ou 1). Réessayez.")