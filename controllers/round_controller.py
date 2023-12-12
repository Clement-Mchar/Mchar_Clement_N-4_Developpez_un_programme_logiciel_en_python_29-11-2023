import random
from models.data import DataManager
from models.round import Round
from views.round_view import RoundView
from controllers.match_controller import MatchController


class RoundController:

    @staticmethod
    def create_round(tournaments, tournament, registered_players):

        while len(tournament.rounds) < tournament.number_of_rounds:
            
            rounds_path = DataManager("./data/rounds.json")
            rounds = rounds_path.load_data_set()

            round_number = len(tournament.rounds) + 1

            new_round = Round(
                id=tournament.id,
                name=f"Round {round_number}",
                matches=[]
            )
            if round_number == 1 :
                players_list = sorted(registered_players, key=lambda x: (x[1], x[0]))
                random.shuffle(players_list)
            else :
                players_list = sorted(registered_players, key=lambda x: (x[2]), reverse=True)

            tournament.rounds.append(f"{new_round.id}")
            rounds.append(new_round.to_dict())

            rounds_path.save_data(new_round.to_dict())
            DataManager.update_tournaments(tournaments)
            MatchController.create_match(rounds, new_round, players_list)
            DataManager.update_rounds(rounds)
        

            
        

        
