from flask import render_template, Blueprint, request, redirect, session
from Utils.utilities import get_all_category, get_all_product
import datetime

"""
Nom du script: 
    back_office.py
Description: 
    Contient la route permettant d'acceder a la page Back Office par les administrateurs
Dernière revue: 
    14 novembre 2023
Par: 
    Yassine Négoce
"""

back_office_bp = Blueprint('back_office', __name__, template_folder='templates')


@back_office_bp.get("/back-office")
def back_office():
    """Route permettant d'afficher la page de back-office accessible par les administrateur.
    Elle affiche les articles présent en base de donnée tout en donnant accès a des options d'ajout,
    de modification et de suppression d'articles"""
    if session.get("user") == "admin":
        error_image = request.args.get('error_image', False)
        error_add_product = request.args.get('error_add_product', False)
        add_product_success = request.args.get('add_product_success', False)
        error_modify_product = request.args.get('error_modify_product', False)
        product_deleted = request.args.get('product_deleted', False)
        today = datetime.date.today()
        list_category = get_all_category()
        list_product = get_all_product()
        return render_template("back-office.html", products=list_product,
                               categories=list_category, today=today, error_image=error_image,
                               error_add_product=error_add_product, add_product_success=add_product_success,
                               error_modify_product=error_modify_product, product_deleted=product_deleted)
    else:
        return redirect('/login')
