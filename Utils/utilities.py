from models.admins import Admins
from models.category import Category
from models.products import Products

"""
Nom du script: 
    utilities.py
Description: 
    Contient les fonctions permettant de récupérer la liste des produits, la 
    liste des categories ainsi que la liste des user présent en base de donnée
Dernière revue: 
    13 novembre 2023
Par: 
    Yassine Négoce
"""


def get_all_category():
    """Fonction permettant de récupérer toutes les categoeries présentent en base de données"""
    list_category = []
    categories = Category.query.all()
    for category in categories:
        list_category.append(category.libelle)
    return list_category


def get_all_product():
    """Fonction permettant de récupérer tous les produits présent en base de
    données sous format json afin de les afficher"""
    list_product = []
    products = Products.query.all()
    for product in products:
        list_product.append(
            {
                "id_product": product._id_product,
                "name": product.name,
                "description": product.description,
                "category_name": product._category_name,
                "image_data": product.image_data,
                "price": product.price,
                "promo_start": product.promo_start,
                "promo_end": product.promo_end,
                "promo_amount": product.promo_amount,
                "new_price": product.price * (1 - (product.promo_amount / 100))
            }
        )
    return list_product


def get_sorted_product(categorie, sens):
    """Fonction récuperant les produit en fonction du choix de categorie et du tri selectionné par l'utilisateur"""
    updated_list_products = []

    if categorie == "Choisir une catégorie":
        if sens:
            updated_products = Products.query.order_by(Products._price.desc()).all()
        else:
            updated_products = Products.query.order_by(Products._price).all()
    else:
        if sens:
            updated_products = Products.query.filter(Products._category_name == categorie).order_by(
                Products._price.desc()).all()
        else:
            updated_products = Products.query.filter(Products._category_name == categorie).order_by(
                Products._price).all()

    for product in updated_products:
        updated_list_products.append(
            {
                "id_product": product._id_product,
                "name": product.name,
                "description": product.description,
                "category_name": product._category_name,
                "image_data": product.image_data,
                "price": product.price,
                "promo_start": product.promo_start,
                "promo_end": product.promo_end,
                "promo_amount": product.promo_amount,
                "new_price": product.price * (1 - (product.promo_amount / 100))
            }
        )
    return updated_list_products


def get_all_users():
    """Fonction qui récupère la liste des user présent en base de données"""
    users_list = []
    users = Admins.query.all()
    for user in users:
        users_list.append(
            {
                "identifiant": user._identifiant,
                "password": user._password,
            }
        )
    return users_list
