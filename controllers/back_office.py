from flask import render_template, Blueprint
from controllers.utilities import get_all_category, get_all_product
import datetime

"""
Nom du script: 
    back_office.py
Description: 
    Contient la route permettant d'acceder a la page Back Office par les administrateurs
Dernière revue: 
    10 novembre 2023
Par: 
    Yassine Négoce
"""

back_office_bp = Blueprint('back_office', __name__, template_folder='templates1')


@back_office_bp.get("/back-office")
def back_office():
    """Route permettant d'afficher la page de back-office accessible par les administrateur.
    Elle affiche les articles présent en base de donnée tout en donnant accès a des options d'ajout,
    de modification et de suppression d'articles"""
    today = datetime.date.today()
    list_category = get_all_category()
    list_product = get_all_product()
    return render_template("back-office.html", products=list_product,
                           categories=list_category, today=today)




