from flask import render_template, Blueprint, request, redirect, url_for

login_bp = Blueprint('login', __name__, template_folder='templates1')


@login_bp.get("/login")
def login():
    return render_template("login.html")


@login_bp.post("/traitement")
def traitement():
    input_login = request.form
    identifiant_login = input_login.get('id')
    password_login = input_login.get('mdp')
    if identifiant_login == 'admin' and password_login == 'admin':
        return redirect(url_for('back_office.back_office'))
    else:
        connexion = False
        return render_template('login.html', connexion=connexion)
