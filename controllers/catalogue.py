import datetime
from flask import render_template, Blueprint, request, jsonify
from Utils.utilities import get_all_category, get_all_product, get_sorted_product

"""
Nom du script: 
    catalogue.py
Description: 
    Regroupe les deux routes pour l'affichage du catalogue (coté visiteurs)
Dernière revue: 
    14 novembre 2023
Par: 
    Yassine Négoce
"""

catalogue_bp = Blueprint('catalogue', __name__, template_folder='templates')


@catalogue_bp.get("/catalogue")
def catalogue():
    """Cette route affiche le catalogue version full articles
    en indiquant les information des produit et les promotions"""
    today = datetime.date.today()
    list_category = get_all_category()
    list_product = get_all_product()
    return render_template("catalogue.html", products=list_product,
                           categories=list_category, today=today)


@catalogue_bp.post("/updated_selection")
def catalogue_update():
    """Cette route gère la mise a jour du catalogue affiché en fonction
    du choix de tri et du choix de la catégorie choisi par l'utilisateur"""
    category_selected = request.json.get('category')
    sort_order = request.json.get('sortOrder')
    today = datetime.date.today()
    if sort_order == "croissant":
        sens = False
    else:
        sens = True
    updated_list_product = get_sorted_product(category_selected, sens)
    updated_products_html = render_template('catalogue-personalised.html',
                                            products=updated_list_product, today=today)
    return jsonify({"productsHTML": updated_products_html})
