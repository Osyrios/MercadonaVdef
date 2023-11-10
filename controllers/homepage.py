from flask import render_template, Blueprint

homepage_bp = Blueprint('homepage', __name__, template_folder='templates')


@homepage_bp.get("/")
def homepage():
    return render_template("index.html")
