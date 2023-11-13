from flask import render_template, Blueprint, request, redirect, url_for, session

from models.admins import Admins

"""
Nom du script: 
    login.py
Description: 
    Contient la route d'affichage du formulaire de connexion ainsi que la fonction de 
    verification des identifiant pour la connexion au back office
Dernière revue: 
    11 novembre 2023
Par: 
    Yassine Négoce
"""

login_bp = Blueprint('login', __name__, template_folder='templates')


@login_bp.get("/login")
def login():
    """Affiche la page de connexion au back office"""
    return render_template("login.html")


@login_bp.post("/traitement")
def traitement():
    """Traite les identifiant envoyé par l'utilisateur pour verifier s'il s'agit bien
    d'un admin et lui permettre l'accès au back office ou lui refuser l'accès si ce n'est pas le cas"""
    if request.method == "POST":
        input_login = request.form
        identifiant_login = input_login.get('id')
        password_login = input_login.get('mdp')

        if identifiant_login == 'admin' and password_login == 'admin':
            session['user'] = 'admin'
            session.permanent = False
            return redirect(url_for('back_office.back_office'))
        else:
            session.pop('user', None)
            connexion = False
            return render_template('login.html', connexion=connexion)
    else:
        return redirect('/login')
