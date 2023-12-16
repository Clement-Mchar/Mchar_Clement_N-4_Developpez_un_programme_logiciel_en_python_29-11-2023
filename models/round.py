class Round:
    def __init__(self, id, tournament_id, start_date, end_date, name, matches):
        self._id = id
        self._tournament_id = tournament_id
        self._matches = matches if matches else []
        self._name = name
        self._start_date = start_date
        self._end_date = end_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tournament_id(self):
        return self._tournament_id

    @tournament_id.setter
    def round_id(self, tournament_id):
        self._tournament_id = tournament_id

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, matches):
        self._matches = matches

    def to_dict(self):
        return {
            "id": self.id,
            "tournament_id": self.tournament_id,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "name": self.name,
            "matches": self.matches
        }
