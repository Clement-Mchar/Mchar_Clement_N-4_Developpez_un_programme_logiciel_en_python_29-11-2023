import random
from models.data import DataManager
from models.round import Round
from views.round_view import RoundView
from controllers.match_controller import MatchController


class RoundController:

    @staticmethod
    def create_round(players, rounds):

        tournaments_path = DataManager("./data/tournaments.json")
        tournaments = tournaments_path.load_data_set()
        tournament = tournaments[-1]
        matches = []
        for round_number in range(1, tournament["number_of_rounds"] +1):
            

            new_round = Round(
                number=round_number,
                name=f"Round {round_number}",
                matches=matches
            )
            if round_number == 1 :
                players_list = sorted(players, key=lambda x: (x["player"]))
            else :
                players_list = sorted(players, key=lambda x: (x["score"]))

            random.shuffle(players_list)
            rounds.append(new_round.name)
            tournament["rounds"].append(new_round.name)
            DataManager.update_tournament(tournaments)
            MatchController.create_match(
                new_round,
                players_list,
                matches,
            )
 
            
        

        
