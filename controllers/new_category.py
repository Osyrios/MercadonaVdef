from flask import render_template, Blueprint
from controllers.utilities import get_all_category

"""
Nom du script: 
    new_category.py
Description: 
    Contient la route permettant d'acceder a la page d'ajout de catégories
Dernière revue: 
    10 novembre 2023
Par: 
    Yassine Négoce
"""

new_category_bp = Blueprint('new_category', __name__, template_folder='templates')


@new_category_bp.get("/new_category")
def new_category():
    """Route affichant la page d'ajout de nouvelles catégories ainsi que recupère les categories pour les afficher"""
    list_category = get_all_category()
    return render_template("new_category.html", categories=list_category)
