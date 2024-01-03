from models.data import DataManager


class ProgramState:
    """Saves and loads program's current state"""

    def __init__(self):
        self.tournaments = []
        self.current_tournament = None
        self.players = []
        self.registered_players = []
        self.played_players = []
        self.tournament_rounds = []
        self.rounds = []
        self.current_round = None
        self.round_matches = []
        self.matches = []
        self.current_match = None
        self.load_initial_data()

    def load_initial_data(self):
        tournaments_path = DataManager("./data/tournaments.json")
        self.tournaments = tournaments_path.load_data_set()

        players_path = DataManager('./data/players.json')
        self.players = players_path.load_data_set()

        rounds_path = DataManager("./data/rounds.json")
        self.rounds = rounds_path.load_data_set()

        matches_path = DataManager("./data/matches.json")
        self.matches = matches_path.load_data_set()
