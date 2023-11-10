import json

from database.database import db


class Category(db.Model):
    _id_category = db.Column('id_category', db.Integer, primary_key=True, autoincrement=True, nullable=True)
    _libelle = db.Column('libelle', db.String, unique=True, nullable=False, )
    # Création de la relation one to many entre la classe Device et la classe Category
    _devices = db.relationship('Products')

    def __init__(self, libelle: str):
        self._libelle = libelle

    # Getter du id_category
    @property
    def category(self):
        return self._id_category

    # Getter du libelle
    @property
    def libelle(self):
        return self._libelle

    # Setter du libelle
    @libelle.setter
    def libelle(self, libelle: str):
        self._libelle = libelle

    def to_json(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "id_category": self.id_category,
            "libelle": self.libelle,
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        return Category(json_dct['libelle'])
