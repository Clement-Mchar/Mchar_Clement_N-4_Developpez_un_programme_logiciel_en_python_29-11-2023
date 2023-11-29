import datetime

class Player:

    def __init__(self, first_name, last_name, birthdate):
        self._last_name = last_name
        self._first_name = first_name
        self._birthdate = birthdate
        self._score = None
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name.isalpha():
            raise ValueError("Le prénom ne doit contenir que des lettres !")
        if len(first_name) > 15 :
            raise ValueError("Le prénom est trop long !")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if not last_name.isalpha():
            raise ValueError("Le nom de famille ne doit contenir que des lettres !")
        if len(last_name) > 20 :
            raise ValueError("Le nom de famille est trop long !")
        self._last_name = last_name
    
    @property
    def birthdate(self):
        return self._birthdate.strftime("%d/%m/%Y")
    
    @birthdate.setter
    def birthdate(self, birthdate):
        self._birthdate = self._validate_birthdate(birthdate)


    @classmethod
    def _validate_birthdate(cls, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            return date_obj
        except ValueError:
            raise ValueError("Le format de la date de naissance doit être JJ/MM/AAAA.")
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": str(self._birthdate)
        }
    
