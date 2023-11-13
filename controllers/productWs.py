from flask import request, Blueprint, redirect, url_for, session
from models.products import Products
from database.database import db
import json
import base64

"""
Nom du script: 
    productWs.py
Description: 
    Contient les fonctions permettant de créer, modifier et supprimer un produit 
Dernière revue: 
    13 novembre 2023
Par: 
    Yassine Négoce
"""

product_ws = Blueprint('ProductWS', __name__, template_folder='templates')


@product_ws.post('/add_product')
def create_product():
    """Fonction permettant la création d'un nouveau produit et l'envoi a la base de donnée en tant qu'objet Products"""
    # traitement de l'images upload par l'uitilsateur afin de la convertire en base64
    # vérifie si une images a été envoyer dans la requete
    if session.get('user') == 'admin':
        if "image_data" in request.files:
            uploaded_image = request.files["image_data"]
            # verifie qu'uploaded_image contient de la donnée
            if uploaded_image:
                # vérification de la catégorie choisie par l'utilisateur
                category_name = request.form.get("category_name")
                if category_name != "choisir une catégorie":
                    image_converted = base64.b64encode(uploaded_image.read()).decode("utf-8")
                    # creation d'un dictionnaire avec les données du formulaire ainsi que l'images en base64
                    form_data = {
                        "id_product": None,
                        "name": request.form.get("name"),
                        "category_name": category_name,
                        "description": request.form.get("description"),
                        "image_data": image_converted,
                        "price": request.form.get("price"),
                        "promo_start": request.form.get("promo_start"),
                        "promo_end": request.form.get("promo_end"),
                        "promo_amount": request.form.get("promo_amount")
                    }
                    # Création d'un nouveau produit "product"
                    new_product = Products.from_json(form_data)
                    # envoi a la base de donnée
                    db.session.add(new_product)
                    db.session.commit()
                    add_product_success = True
                    return redirect(url_for('back_office.back_office', add_product_success=add_product_success))
                else:
                    error_add_product = True
                    return redirect(url_for('back_office.back_office', error_add_product=error_add_product))
            else:
                error_image = True
                return redirect(url_for('back_office.back_office', error_image=error_image))
        else:
            error_image = True
            return redirect(url_for('back_office.back_office', error_image=error_image))
    else:
        return redirect(url_for('login.login'))


@product_ws.post('/update_product/<id_product>')
def modify_product(id_product: int):
    """Fonction permettant de modifier les informations d'un produit selectionné"""
    if session.get('user') == 'admin':
        try:
            # Préparation de l'update du produit, on récupère l'ancien objet
            old_product: Products = db.session.query(Products).filter(Products._id_product == id_product).one()

            # Stockage de la nouvelle image si upload sinon récupération de l'ancienne image
            old_image = old_product.image_data

            if "image_data" in request.files and request.files["image_data"].filename:
                new_updated_image = base64.b64encode(request.files["image_data"].read()).decode("utf-8")
            else:
                new_updated_image = old_image

            # Formatage en JSON du "nouveau" produit avec les modifications envoyées par l'utilisateur
            new_informations = {
                "id_product": int(request.form.get("id_product")),
                "name": request.form.get("name"),
                "category_name": old_product._category_name,
                "description": request.form.get("description"),
                "image_data": new_updated_image if "image_data" in request.files else old_image,
                "price": float(request.form.get("price")),
                "promo_start": request.form.get("promo_start"),
                "promo_end": request.form.get("promo_end"),
                "promo_amount": int(request.form.get("promo_amount"))
            }
            # Suppression de l'ancien produit
            db.session.delete(old_product)
            db.session.commit()
            # Création du nouveau produit
            updated_product = Products.from_json(new_informations)
            db.session.add(updated_product)
            db.session.commit()
            error_modify_product = False
            return redirect(url_for('back_office.back_office', error_modify_product=error_modify_product))
        except Exception as e:
            print(f"Erreur lors de la modification du produit : {e}")
            db.session.rollback()
            error_modify_product = True
            return redirect(url_for('back_office.back_office', error_modify_product=error_modify_product))
    else:
        return redirect(url_for('login.login'))


@product_ws.post('/<id_product>')
def delete_product(id_product: int):
    """Fonction permettant la suppression de l'article selectionné"""
    if session.get('user') == 'admin':
        data: Products = db.session.query(Products).filter(Products._id_product == id_product).one()
        if type(data) is not None:
            db.session.delete(data)
            db.session.commit()
            product_deleted = True
            return redirect(url_for('back_office.back_office', product_deleted=product_deleted))
        else:
            product_deleted = False
            return redirect(url_for('back_office.back_office', product_deleted=product_deleted))
    else:
        return redirect(url_for('login.login'))
