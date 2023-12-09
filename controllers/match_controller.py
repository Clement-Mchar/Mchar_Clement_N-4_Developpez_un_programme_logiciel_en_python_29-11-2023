import random
from models.match import Match
from views.round_view import RoundView
from models.data import DataManager

class MatchController :

    @staticmethod
    def create_match(tournament, new_round, players_list):

        displayed_matches = []
        match_players = zip(players_list[::2], players_list[1::2])
        match_number = len(displayed_matches) +1

        for match_number, (
            player_1, 
            player_2
        ) in enumerate(match_players, start=1):
            print(player_1.first_name, player_1.score)
            match = Match(
                id=tournament.id,
                name=f"Match N.{match_number}:",
                player_1=str(player_1),
                player_2=str(player_2),
                result=""
            )
            displayed_player_1 = f"{player_1.first_name} {player_1.last_name}"
            displayed_player_2 = f"{player_2.first_name} {player_2.last_name}"
            match_tuple = (player_1, player_2)
            new_round.matches.append(match_tuple)
            displayed_match = [
                match.name,
                displayed_player_1,
                displayed_player_2
            ]
            displayed_matches.append(displayed_match)
        RoundView.display_round_view(new_round, displayed_matches)
        print(displayed_matches)
        

        RoundView.display_results(displayed_matches)
        

        