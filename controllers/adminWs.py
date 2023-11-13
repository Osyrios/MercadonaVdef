from flask import Blueprint, request, redirect, url_for
from database.database import db
from models.admins import Admins

"""
Nom du script: 
    adminWs.py
Description: 
    Contient la fonction de création de nouvel utilisateur
Dernière revue: 
    13 novembre 2023
Par: 
    Yassine Négoce
"""

admin_ws = Blueprint('admin_ws', __name__, template_folder='templates')


@admin_ws.post('/create-user')
def create_user():
    """Fonction qui créer un nouvel utilisateur en base de donnée ayant accès au abck office"""
    try:
        data = {
            "identifiant": request.form.get('identifiant'),
            "password": request.form.get('password'),
        }
        new_user = Admins.from_json(data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('new_admin.new_admin'))
    except Exception as e:
        print(e)
        return redirect(url_for('new_admin.new_admin'))
