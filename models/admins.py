from Utils.Password import encode_password
from database.database import db

"""
Nom du script: 
    admins.py
Description: 
    initialisation de la classe admins
Dernière revue: 
    13 novembre 2023
Par: 
    Yassine Négoce
"""


class Admins(db.Model):
    _identifiant = db.Column('identifiant', db.String, primary_key=True)
    _password = db.Column('password', db.String(100))

    def __init__(self, identifiant: str, password: str):
        self._identifiant = identifiant
        self._password = encode_password(password).decode(encoding='utf-8')

    # Getter de l'identifiant
    @property
    def identifiant(self):
        return self._identifiant

    # Getter du mot de passe
    @property
    def password(self):
        return self.password

    # Setter du mot de passe
    @password.setter
    def password(self, password):
        self.password = password

    # Passage d'objet python à objet json
    def to_json(self):
        return self.__str__()

    # Définition de Iter, appelé par Str
    def __iter__(self):
        yield from {
            "identifiant": self._identifiant,
        }.items()

    # Passage d'un objet Json en un objet python
    @staticmethod
    def from_json(json_dct):
        return Admins(json_dct["identifiant"],
                      json_dct["password"])
