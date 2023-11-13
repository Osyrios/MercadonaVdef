from flask import render_template, Blueprint, redirect, url_for, session
from models.products import Products

"""
Nom du script: 
    product_update.py
Description: 
    Contient la route permettant d'accèder a la page de modification ou de suppression d'un produit selectionner 
    depuis le back office
Dernière revue: 
    11 novembre 2023
Par: 
    Yassine Négoce
"""

product_update_bp = Blueprint('product_update', __name__, template_folder='templates')


@product_update_bp.get("/product_update/<int:product_id>")
def product_update(product_id):
    """Fonction qui recupère le produit selectionné par l'administrateur et stock les info de ce
    produit afin des les afficher dans le template de modification de produit"""
    if session["user"] == 'admin':
        product = Products.query.get(product_id)
        if product is not None:
            product_to_modify = {
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
            return render_template("product-update.html", product_to_modify=product_to_modify)
        else:
            return redirect(url_for('back_office.back_office'))
    else:
        return redirect("/login")
