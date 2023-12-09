class Round:
    def __init__(self, id, name=None, matches=None):
        self._id = id
        self._matches = matches if matches else []
        self._name = name

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
            "name": self.name,
            "matches": self.matches
        }
