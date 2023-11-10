from models import products
from models.category import Category
from models.products import Products


def get_all_category():
    list_category = []
    categories = Category.query.all()
    for category in categories:
        list_category.append(category.libelle)
    return list_category


def get_all_product():
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
    updated_list_products = []

    if categorie == "Choisir une catégorie" :
        if sens:
            updated_products = Products.query.order_by(Products._price.desc()).all()
        else:
            updated_products = Products.query.order_by(Products._price).all()
    else:
        if sens:
            updated_products = Products.query.filter(Products._category_name == categorie).order_by(Products._price.desc()).all()
        else:
            updated_products = Products.query.filter(Products._category_name == categorie).order_by(Products._price).all()

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
