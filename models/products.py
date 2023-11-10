import json

from database.database import db


class Products(db.Model):
    _id_product = db.Column('id_product', db.Integer, primary_key=True, autoincrement=True, nullable=True)
    _name = db.Column('name', db.String(70), nullable=False)
    _description = db.Column('description', db.Text, nullable=False)
    _price = db.Column('price', db.Float, nullable=False)
    _image_data = db.Column('image_data', db.Text, nullable=False)
    _category_name = db.Column('category_name', db.String, db.ForeignKey('category.libelle'), nullable=False)
    _promo_start = db.Column('promo_start', db.Date, nullable=True)
    _promo_end = db.Column('promo_end', db.Date, nullable=True)
    _promo_amount = db.Column('promo_amount', db.Integer, nullable=True)

    # constructor
    def __init__(self, id_product: int, name: str, category_name: str, description: str, price: float, image_data: str, promo_start,
                 promo_end, promo_amount: int):
        self._id_product = id_product
        self._name = name
        self._category_name = category_name
        self._description = description
        self._price = price
        self._image_data = image_data
        self._promo_start = promo_start
        self._promo_end = promo_end
        self._promo_amount = promo_amount

    # Getter de l'ID du produit
    @property
    def id(self):
        return self._id_product

    # Getter du name
    @property
    def name(self):
        return self._name

    # Setter du name
    @name.setter
    def name(self, name: str):
        self._name = name

    # Getter du category_name
    @property
    def category(self):
        return self._category_name

    # Getter de la description
    @property
    def description(self):
        return self._description

    # Setter de la description
    @description.setter
    def description(self, description: str):
        self._description = description

    # Getter du price
    @property
    def price(self):
        return self._price

    # Setter du price
    @price.setter
    def price(self, price: float):
        self._price = price

    @property
    def image_data(self):
        return self._image_data

    # Setter du images
    @image_data.setter
    def image_data(self, image_data: str):
        self._image_data = image_data

    # Getter de la date de debut de promo
    @property
    def promo_start(self):
        return self._promo_start

    # Setter de la date de debut de promo
    @promo_start.setter
    def promo_start(self, promo_start):
        self._promo_start = promo_start

    # Getter de la date de fin de promo
    @property
    def promo_end(self):
        return self._promo_end

    # Setter de la date de fin de promo
    @promo_end.setter
    def promo_end(self, promo_end):
        self._promo_end = promo_end

    # Getter du montant de la promo (en poucentage)
    @property
    def promo_amount(self):
        return self._promo_amount

    # Setter du montant de la promo (en poucentage)
    @promo_amount.setter
    def promo_amount(self, promo_amount):
        self._promo_amount = promo_amount

    # Renvoi de l'objet python en JSON
    def to_json(self):
        return self.__str__()

    # Conversion de l'objet python en JSON - dict(self) appelle __iter__
    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    # Renvoi d'un dictionnaire de la classe actuelle
    def __iter__(self):
        yield from {
            "id_product": self._id_product,
            "name": self._name,
            "category_name": self._category_name,
            "description": self._description,
            "price": self._price,
            "image_data": self._image_data,
            "promo_start": self._promo_start,
            "promo_end": self._promo_end,
            "promo_amount": self._promo_amount
        }.items()

    # mappage de la création d'un nouveau produit a partir de la reponse Json du formulaire de création
    @staticmethod
    def from_json(json_dct):
        return Products(json_dct["id_product"],
                        json_dct["name"],
                        json_dct["category_name"],
                        json_dct["description"],
                        json_dct["price"],
                        json_dct["image_data"],
                        json_dct["promo_start"],
                        json_dct["promo_end"],
                        json_dct["promo_amount"]
                        )