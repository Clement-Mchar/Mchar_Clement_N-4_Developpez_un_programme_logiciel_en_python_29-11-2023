class Round:
    def __init__(self, number, name=None, matches=None):
        self._number = number
        self._matches = matches if matches else []
        self._name = name

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
    def matches(self):
        return self._matches

    def to_dict(self):
        return {
            "number": self.number,
            "name": self.name,
            "matches": self.matches

        }