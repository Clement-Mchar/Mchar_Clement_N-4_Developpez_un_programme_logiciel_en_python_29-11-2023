import random
from models.data import DataManager
from models.round import Round
from views.round_view import RoundView
from controllers.match_controller import MatchController


class RoundController:

    @staticmethod
    def create_round(tournaments, tournament, registered_players):

        while len(tournament.rounds) < tournament.number_of_rounds:
            
            print(registered_players)
            rounds_path = DataManager("./data/rounds.json")

            round_number = len(tournament.rounds) + 1

            new_round = Round(
                id=tournament.id,
                name=f"Round {round_number}",
                matches=[]
            )
            if round_number == 1 :
                players_list = sorted(registered_players, key=lambda x: (x.last_name, x.first_name))
                random.shuffle(players_list)
            else :
                players_list = sorted(registered_players, key=lambda x: (x.score))

            tournament.rounds.append(f"{new_round.id}")
            DataManager.update_tournaments(tournaments)
            rounds_path.save_data(new_round.to_dict())
            MatchController.create_match(tournament, new_round, players_list)


            
        

        
