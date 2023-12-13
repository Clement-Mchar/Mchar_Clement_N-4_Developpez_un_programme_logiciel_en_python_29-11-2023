import random
import datetime
from models.data import DataManager
from models.round import Round
from controllers.match_controller import MatchController


class RoundController:

    @staticmethod
    def create_round(tournaments, tournament, registered_players):

        while len(tournament.rounds) < tournament.number_of_rounds:

            rounds_path = DataManager("./data/rounds.json")
            rounds = rounds_path.load_data_set()

            round_number = len(tournament.rounds) + 1
            start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

            new_round = Round(
                id=tournament.id,
                start_date=start_date,
                end_date="",
                name=f"Round {round_number}",
                matches=[]
            )

            tournament.rounds.append(f"{new_round.id}")
            rounds.append(new_round.to_dict())

            rounds_path.save_data(new_round.to_dict())
            DataManager.update_tournaments(tournaments)

            if round_number == 1:
                players_list = sorted(
                    registered_players,
                    key=lambda x: (x[1], x[0])
                )

                random.shuffle(players_list)
            else:
                players_list = sorted(
                    registered_players,
                    key=lambda x: (x[2]),
                    reverse=True
                )

            MatchController.create_match(
                tournament,
                rounds,
                new_round,
                players_list
            )

            number_of_matches = tournament.number_of_players / 2
            if len(new_round.matches) == number_of_matches:

                end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                rounds[-1]["end_date"] = end_date
                print(f"Date de fin du round : {end_date} .")
                DataManager.update_rounds(rounds)
