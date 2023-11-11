from flask import Blueprint, session, redirect, url_for

"""
Nom du script:
    logout.py
Description:
    Contient la fonction permettant la deconnexion de l'administrateur
Dernière revue:
    11 novembre 2023
Par:
    Yassine Négoce
"""

logout_bp = Blueprint('logout', __name__, template_folder='templates')


@logout_bp.post("/logout")
def logout():
    """Fonction qui deconnecte l'administrateur et le renvoi sur le catalogue"""
    session.pop('user', None)
    print('utilisateur deconnecté')
    return redirect(url_for('catalogue.catalogue'))
