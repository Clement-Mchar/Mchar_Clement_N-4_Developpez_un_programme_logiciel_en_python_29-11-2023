class Tournament:

    def __init__(
                self,
                id,
                name,
                place,
                start_date,
                end_date,
                rounds,
                players,
                notes,
                number_of_players,
                number_of_rounds=4):

        self._id = id
        self._name = name
        self._place = place
        self._start_date = start_date
        self._end_date = end_date
        self._rounds = rounds
        self._players = players
        self._notes = notes
        self._number_of_players = number_of_players
        self._number_of_rounds = number_of_rounds

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = self._validate_name(name)

    @classmethod
    def _validate_name(cls, name):
        if len(name) > 30:
            raise ValueError("le nom du tournoi est trop long")

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, place):
        self._place = self._validate_place(place)

    @classmethod
    def _validate_place(cls, place):
        if len(place) > 40:
            raise ValueError("Le nom du lieu est trop long !")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def number_of_players(self):
        return self._number_of_players

    @number_of_players.setter
    def number_of_players(self, number_of_players):
        self._number_of_players = self._validate_number_of_players(
            number_of_players
        )

    @classmethod
    def _validate_number_of_players(cls, number_of_players):
        if not isinstance(number_of_players, int):
            raise ValueError("Le nombre de rounds doit être un entier.")
        if not (2 <= number_of_players <= 64):
            raise ValueError("Minimum 2 joueurs, maximum 10 joueurs.")
        if not (number_of_players % 2 == 0):
            raise ValueError("Le nombre de joueurs doit être pair !")

    @property
    def number_of_rounds(self):
        return self._number_of_rounds

    @number_of_rounds.setter
    def number_of_rounds(self, number_of_rounds):
        self._number_of_rounds = self._validate_number_of_rounds(
            number_of_rounds
        )

    @classmethod
    def _validate_number_of_rounds(cls, number_of_rounds):
        if not isinstance(number_of_rounds, int):
            raise ValueError("Le nombre de rounds doit être un entier.")
        if not (2 <= number_of_rounds <= 10):
            raise ValueError("Minimum 2 rounds, maximum 10 rounds.")

    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, rounds):
        self._rounds = rounds

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "number_of_players": int(self.number_of_players),
            "number_of_rounds": int(self.number_of_rounds),
            "players": self.players,
            "rounds": self.rounds,
            "notes": self.notes
        }
