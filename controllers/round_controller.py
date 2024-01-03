import random
import datetime
from models.data import DataManager
from models.round import Round
from controllers.match_controller import MatchController


class RoundController:

    @staticmethod
    def create_round(program_state):
        tournaments = program_state.tournaments
        tournament = program_state.current_tournament
        registered_players = program_state.registered_players
        rounds = program_state.rounds
        program_state.tournament_rounds = []
        tournament_rounds = program_state.tournament_rounds
        program_state.round_matches = []

        from controllers.tournament_controller import TournamentController

        while len(tournament['rounds']) < tournament['number_of_rounds']:

            rounds_path = DataManager("./data/rounds.json")
            round_number = len(tournament['rounds']) + 1
            start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

            new_round = Round(
                id=len(rounds) + 1,
                tournament_id=tournament['id'],
                start_date=start_date,
                end_date="",
                name=f"Round {round_number}",
                matches=[]
            )

            tournament['rounds'].append(round_number)
            tournament_rounds.append(new_round.to_dict())

            rounds.append(new_round.to_dict())
            rounds_path.save_data(new_round.to_dict())
            DataManager.update_tournaments(tournaments)

            if round_number == 1:
                players_list = sorted(
                    registered_players,
                    key=lambda x: (x[1])
                )

                random.shuffle(players_list)
                program_state.registered_players = players_list
            else:
                players_list = sorted(
                    registered_players,
                    key=lambda x: (x[2]),
                    reverse=True
                )

                program_state.registered_players = players_list

            program_state.current_round = rounds[-1]
            MatchController.create_match(
                program_state
            )

            number_of_matches = tournament['number_of_players'] / 2

            if len(new_round.matches) == number_of_matches:
                end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                rounds[-1]["end_date"] = end_date
                print(f"Date de fin du round : {end_date} .")
                DataManager.update_rounds(rounds)

        TournamentController.handle_tournament_ranking(program_state)
