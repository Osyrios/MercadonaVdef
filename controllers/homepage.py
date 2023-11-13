from flask import render_template, Blueprint

"""
Nom du script: 
    homepage.py
Description: 
    Contient la route permettant l'accès à la page d'accueil
Dernière revue: 
    13 novembre 2023
Par: 
    Yassine Négoce
"""

homepage_bp = Blueprint('homepage', __name__, template_folder='templates')


@homepage_bp.get("/")
def homepage():
    """Renvoi l'affichage du template de la page d'accueil"""
    return render_template("index.html")
