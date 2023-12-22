import random
import datetime

from models.data import DataManager
from models.round import Round
from controllers.match_controller import MatchController


class RoundController:

    @staticmethod
    def create_round(tournaments, tournament, registered_players, players_scores):
        from controllers.tournament_controller import TournamentController
        
        while len(tournament.rounds) < tournament.number_of_rounds:

            rounds_path = DataManager("./data/rounds.json")
            rounds = rounds_path.load_data_set()

            round_number = len(tournament.rounds) + 1
            start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

            new_round = Round(
                id=len(rounds) + 1,
                tournament_id=tournament.id,
                start_date=start_date,
                end_date="",
                name=f"Round {round_number}",
                matches=[]
            )

            tournament.rounds.append(new_round.id)
            rounds.append(new_round.to_dict())

            rounds_path.save_data(new_round.to_dict())
            DataManager.update_tournaments(tournaments)

            if round_number == 1:
                players_list = sorted(
                    registered_players,
                    key=lambda x: (x[1])
                )

                random.shuffle(players_list)
            else:
                sorted(
                    players_scores,
                    key=lambda x: (x[2]),
                    reverse=True
                )
                print(players_scores)
            MatchController.create_match(
                rounds,
                new_round,
                players_list,
                players_scores
            )

            number_of_matches = tournament.number_of_players / 2

            if len(new_round.matches) == number_of_matches:

                end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                rounds[-1]["end_date"] = end_date
                print(f"Date de fin du round : {end_date} .")
                DataManager.update_rounds(rounds)

        TournamentController.handle_tournament_ranking(players_scores)
