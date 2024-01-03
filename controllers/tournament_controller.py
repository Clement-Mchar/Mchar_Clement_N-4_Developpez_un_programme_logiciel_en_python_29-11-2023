import datetime
from models.tournament import Tournament
from models.data import DataManager
from views.tournament_view import TournamentView
from controllers.player_controller import PlayerController


class TournamentController:

    """Handles tournament creation"""
    @staticmethod
    def create_tournament(program_state):
        tournaments_path = DataManager("./data/tournaments.json")
        tournaments = program_state.tournaments
        tournament_info = TournamentView.display_tournament_creation()
        program_state.played_players = []

        try:
            tournament_id = len(tournaments) + 1
            start_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            tournament = Tournament(
                id=tournament_id,
                name=tournament_info[0],
                place=tournament_info[1],
                start_date=start_date,
                end_date="",
                rounds=[],
                players=[],
                notes=tournament_info[4],
                ranking=[],
                is_over=False,
                number_of_players=tournament_info[2],
                number_of_rounds=tournament_info[3]
            )

            tournament._validate_name(name=tournament_info[0])
            tournament._validate_place(place=tournament_info[1])
            tournament._validate_number_of_players(
                number_of_players=tournament_info[2]
            )
            tournament._validate_number_of_rounds(
                number_of_rounds=tournament_info[3]
            )

            tournaments.append(tournament.to_dict())
            tournaments_path.save_data(tournament.to_dict())
            program_state.current_tournament = tournaments[-1]
        except ValueError as e:
            print(f"Erreur {e}")
            TournamentView.display_tournament_creation()
        PlayerController.register_a_player(program_state)

    def handle_tournament_ranking(program_state):

        TournamentView.display_tournament_ranking(program_state)
        TournamentController.end_tournament(program_state)

    def end_tournament(program_state):

        tournaments = program_state.tournaments
        tournament = program_state.current_tournament
        if len(tournament['rounds']) == tournament['number_of_rounds']:
            end_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            tournaments[-1]["end_date"] = end_date
            print("Date de fin du tournoi mise à jour.")
            tournaments[-1]["is_over"] = True
            DataManager.update_tournaments(tournaments)
        program_state.registered_players = []
        program_state.round_matches = []
        program_state.tournament_rounds = []
