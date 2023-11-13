from flask import render_template, Blueprint, url_for, redirect, session
from Utils.utilities import get_all_category

"""
Nom du script: 
    new_category.py
Description: 
    Contient la route permettant d'acceder a la page d'ajout de catégories
Dernière revue: 
    13 novembre 2023
Par: 
    Yassine Négoce
"""

new_admin_bp = Blueprint('new_admin', __name__, template_folder='templates')


@new_admin_bp.get("/new-admin")
def new_admin():
    """Route affichant la page d'ajout de nouvelles catégories ainsi que recupère les categories pour les afficher"""
    return render_template("create-user.html")

