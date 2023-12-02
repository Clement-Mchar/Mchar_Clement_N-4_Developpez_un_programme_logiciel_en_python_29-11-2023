class Match:

    def __init__(self, name, players):
        self._name = name
        self._players = players
        self._result = None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        self._result = result