import random
import datetime
from rich.console import Console
from rich.table import Table
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
                    key=lambda x: (x[2], x[1])
                )

                random.shuffle(players_list)
            else:
                players_list = sorted(
                    registered_players,
                    key=lambda x: (x[3]),
                    reverse=True
                )
            MatchController.create_match(
                rounds,
                new_round,
                players_list,
            )

            number_of_matches = tournament.number_of_players / 2

            if len(new_round.matches) == number_of_matches:

                end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                rounds[-1]["end_date"] = end_date
                print(f"Date de fin du round : {end_date} .")
                DataManager.update_rounds(rounds)
        RoundController.handle_ranking(registered_players)

    def handle_ranking(registered_players):
        print("Voici le classement du tournoi :")
        players_list = sorted(
                    registered_players,
                    key=lambda x: (x[3]),
                    reverse=True
                )
        print(players_list)
        table = Table(show_header=True, header_style="cyan")
        table.add_column("Place", style="white", justify="right")
        table.add_column("Prénom", style="white")
        table.add_column("Nom", style="white")
        table.add_column("Score", style="white")

        for rank, player in enumerate(players_list, start=1):
            table.add_row(
                str(rank),
                player[1],
                player[2],
                str(player[3])
            )
        console = Console()
        console.print(table)
