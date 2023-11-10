import json

from flask import render_template, Blueprint, request, redirect, url_for
from controllers.utilities import get_all_category, get_all_product
import datetime

back_office_bp = Blueprint('back_office', __name__, template_folder='templates1')


@back_office_bp.get("/back-office")
def back_office():
    today = datetime.date.today()
    list_category = get_all_category()
    list_product = get_all_product()
    return render_template("back-office.html", products=list_product,
                           categories=list_category, today=today)




