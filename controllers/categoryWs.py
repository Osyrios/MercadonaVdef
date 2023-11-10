import json

from flask import Blueprint, request, jsonify, redirect

from database.database import db
from models.category import Category

category_ws = Blueprint("categoryWs", __name__, template_folder='templates1')


@category_ws.get('/category')
def get_all_category():
    data: list[Category] = db.session.query(Category).all()
    db.session.commit()
    return json.dumps(data, default=Category.to_json)


@category_ws.post('/add_category')
def create_category():
    try:
        libelle_input = request.form.get("libelle")
        libelle_input_corrected = libelle_input.capitalize()

        data = {
            "libelle": libelle_input_corrected
            }

        new_category: Category = Category.from_json(data)

        db.session.add(new_category)
        db.session.commit()
        return redirect('/new_category')
    except Exception as e:
        print("error :", str(e))
        return jsonify({"success": False}), 400
