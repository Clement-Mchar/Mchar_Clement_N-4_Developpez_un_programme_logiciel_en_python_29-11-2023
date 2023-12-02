import random
from models.data import DataManager
from models.round import Round
from models.match import Match

class RoundController:
    
    @staticmethod
    def create_round(registered_players):

        tournaments_path = DataManager("./data/tournaments.json")
        tournaments = tournaments_path.load_data_set()
        tournament = tournaments[-1]

        

        for _ in range(1, tournament["number_of_rounds"] + 1):
            rounds = tournament["rounds"]
            round_number = len(rounds) +1
            
            new_round = Round(number=round_number,
                        name=f"Round {round_number}",
                        matches=[] )
            
            players_list = sorted(registered_players)

            random.shuffle(players_list)
            print(registered_players)

            rounds_path = DataManager(f"./tournaments/Tournoi_N°{tournament["number"]}"
                          f"_{tournament["name"]}/"
                          f"{new_round.name}.json")

            tournament["rounds"].append(new_round.name)
        
        rounds_path.save_data(new_round.to_dict())        
        tournaments_path.save_data(tournament)


