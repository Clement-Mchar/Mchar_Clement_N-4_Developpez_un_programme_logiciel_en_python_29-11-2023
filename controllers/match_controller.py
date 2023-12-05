from models.match import Match
from views.round_view import RoundView
from models.data import DataManager

class MatchController :

    @staticmethod
    def match_handler(new_round, players_list, matches):
        tournaments_path = DataManager("./data/tournaments.json")
        tournaments = tournaments_path.load_data_set()
        tournament = tournaments[-1]
        rounds_path = DataManager(
            f"./tournaments/Tournoi_N°{tournament['number']}_"
            f"{tournament['name']}/{new_round.name}.json"
        )
        rounds_path.load_data_set()
        
        matches = []
        
        match_players = list(zip(players_list[::2], players_list[1::2]))

        for match_number, (player_1, player_2) in enumerate(match_players, start=1):
            match = Match(
                number=match_number,
                name=f"Match N°{match_number}:",
                player_1=player_1,
                player_2=player_2
            )
            matches.append(match.to_dict())
            
        new_round.matches = matches
        rounds_path.save_data(new_round.to_dict())
                
        RoundView.display_round_view(new_round, matches)