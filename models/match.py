class Match:

    def __init__(self, number, name, player_1, player_2, result):
        self._number = number
        self._name = name
        self._player_1 = player_1
        self._player_2 = player_2
        self._result = result

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def player_1(self):
        return self._player_1

    @player_1.setter
    def player_1(self, player_1):
        self._player_1 = player_1
    @property
    def player_2(self):
        return self._player_2

    @player_2.setter
    def player_2(self, player_2):
        self._player_2 = player_2

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        self._result = result

    def to_dict(self):
        return {
            "number": self.number,
            "name": self.name,
            "player_1": self.player_1,
            "player_2": self.player_2,
            "result": self.result
            }