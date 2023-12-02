import random
from models.data import DataManager
from models.round import Round


class RoundController:

    @staticmethod
    def create_round(players):

        tournaments_path = DataManager("./data/tournaments.json")
        tournaments = tournaments_path.load_data_set()
        tournament = tournaments[-1]

        for _ in range(1, tournament["number_of_rounds"] + 1):
            rounds = tournament["rounds"]
            round_number = len(rounds) + 1

            new_round = Round(
                            number=round_number,
                            name=f"Round {round_number}",
                            matches=[]
                            )

            players_list = sorted(players)

            random.shuffle(players_list)
            print(players)

            rounds_path = DataManager(
                                    "./tournaments/Tournoi_N°"
                                    f"{tournament["number"]}"
                                    f"_{tournament["name"]}/"
                                    f"{new_round.name}.json"
                                    )

            tournament["rounds"].append(new_round.name)
            DataManager.update_tournament(tournaments)

        rounds_path.save_data(new_round.to_dict())
