import random
from models.match import Match
from views.round_view import RoundView
from models.data import DataManager

class MatchController :

    @staticmethod
    def create_match(new_round, players_list, matches):
        tournaments_path = DataManager("./data/tournaments.json")
        tournaments = tournaments_path.load_data_set()
        tournament = tournaments[-1]
        rounds_path = DataManager(
            f"./tournaments/Tournoi_N°{tournament['number']}_"
            f"{tournament['name']}/{new_round.name}.json"
        )
        rounds_path.load_data_set()

        matches = []
        
        displayed_matches = []
        
        match_players = list(zip(players_list[::2], players_list[1::2]))

        for match_number, (
            player_1, 
            player_2
        ) in enumerate(match_players, start=1):

            match = Match(
                number=match_number,
                name=f"Match N.{match_number}:",
                player_1=str(player_1),
                player_2=str(player_2),
                result=""
            )
            match_tuple = (player_1, player_2)
            new_round.matches.append(match_tuple)

            displayed_match = [
                match.name,
                player_1["player"],
                player_2["player"]
            ]
            
            displayed_matches.append(displayed_match)
            matches.append(match)
            MatchController.match_handler(match, match_tuple)
        
        RoundView.display_round_view(new_round, displayed_matches)
        
        
        rounds_path.save_data(new_round.to_dict())
        RoundView.display_results(matches)
        
    @staticmethod
    def match_handler(match, match_tuple):


        players_score = [0, 0.5, 1]
        random.shuffle(players_score)
        player_1_score = players_score[0]


        if player_1_score == 0:
            match_tuple[1]["score"] += 1
            match.result = f"{match_tuple[1]["player"]} a gagné le match !"
        elif player_1_score == 0.5:
            match_tuple[0]["score"] += 0.5
            match_tuple[1]["score"] += 0.5
            match.result = "Match nul !"
        elif player_1_score == 1:
            match_tuple[0]["score"] += 1
            match.result = f"{match_tuple[0]["player"]} a gagné le match !"
        
        for player in match_tuple:
            if player["score"] % 1 == 0:
                player["score"] = int(player["score"])
        