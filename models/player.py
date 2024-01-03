import datetime


class Player:
    """Sets the model for the player object's creation"""

    def __init__(
        self,
        id,
        first_name,
        last_name,
        birthdate,
    ):

        self._id = id
        self._last_name = last_name
        self._first_name = first_name
        self._birthdate = birthdate
        self._score = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._validate_first_name(first_name)
        self._first_name = first_name

    @classmethod
    def _validate_first_name(cls, first_name):
        if not first_name.isalpha():
            raise ValueError("Le prénom ne doit contenir que des lettres !")
        if len(first_name) > 15:
            raise ValueError("Le prénom est trop long !")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._validate_last_name(last_name)
        self._last_name = last_name

    @classmethod
    def _validate_last_name(cls, last_name):
        if not last_name.isalpha():
            raise ValueError("Le nom ne doit contenir que des lettres !")
        if len(last_name) > 20:
            raise ValueError("Le nom est trop long !")

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        self._birthdate = self._validate_birthdate(birthdate)

    @classmethod
    def _validate_birthdate(cls, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            return date_obj
        except ValueError:
            raise ValueError("Format : ""JJ/MM/AAAA")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"name: {self.first_name} {self.last_name}, score: {self.score}"

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": str(self._birthdate)
        }
