import json
from flask import Blueprint, request, jsonify, redirect, session, url_for
from database.database import db
from models.category import Category

"""
Nom du script: 
    categoryWs.py
Description: 
    Contient les fonctions d'ajout des catégories en base de données
Dernière revue: 
    11 novembre 2023
Par: 
    Yassine Négoce
"""

category_ws = Blueprint("categoryWs", __name__, template_folder='templates')


@category_ws.post('/add_category')
def create_category():
    """Cette fonction permet la création d'une catégorie d'après le libellé inscrit
    par l'administrateur et l'envoi en base de donnée. La donnée inscrite par l'utilisateur
    est transformer avant l'envoi a la base de donnée afin que le nom de la catégorie soit
    formater avec la premiere lettre en majuscule"""
    if session.get('user') == 'admin':
        try:
            libelle_input = request.form.get("libelle")
            libelle_input_corrected = libelle_input.capitalize()

            data = {
                "libelle": libelle_input_corrected
            }

            new_category: Category = Category.from_json(data)

            db.session.add(new_category)
            db.session.commit()

            added_category = True
            return redirect(url_for('new_category.new_category', added_category=added_category))
        except Exception as e:
            added_category = False
            return redirect(url_for('new_category.new_category', added_category=added_category))
    else:
        return redirect(url_for('login.login'))
