import json
from flask import Blueprint, request, jsonify, redirect
from database.database import db
from models.category import Category

"""
Nom du script: 
    categoryWs.py
Description: 
    Contient les fonctions d'ajout et de récupération des catégories en base de données
Dernière revue: 
    10 novembre 2023
Par: 
    Yassine Négoce
"""

category_ws = Blueprint("categoryWs", __name__, template_folder='templates1')


@category_ws.get('/category')
def get_all_category():
    """Cette fonction permet de récupérer toutes les catégories présentent dans la base de donnée"""
    data: list[Category] = db.session.query(Category).all()
    db.session.commit()
    return json.dumps(data, default=Category.to_json)


@category_ws.post('/add_category')
def create_category():
    """Cette fonction permet la création d'une catégorie d'après le libellé inscrit
    par l'administrateur et l'envoi en base de donnée. La donnée inscrite par l'utilisateur
    est transformer avant l'envoi a la base de donnée afin que le nom de la catégorie soit
    formater avec la premiere lettre en majuscule"""
    try:
        libelle_input = request.form.get("libelle")
        libelle_input_corrected = libelle_input.capitalize()

        data = {
            "libelle": libelle_input_corrected
            }

        new_category: Category = Category.from_json(data)

        db.session.add(new_category)
        db.session.commit()
        return redirect('/new_category')
    except Exception as e:
        print("error :", str(e))
        return jsonify({"success": False}), 400
