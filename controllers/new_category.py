from flask import render_template, Blueprint
from controllers.utilities import get_all_category

new_category_bp = Blueprint('new_category', __name__, template_folder='templates')


@new_category_bp.get("/new_category")
def new_category():
    list_category = get_all_category()
    return render_template("new_category.html", categories=list_category)
