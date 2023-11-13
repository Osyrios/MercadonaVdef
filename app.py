from flask import Flask
from sqlalchemy import inspect
from controllers.adminWs import admin_ws
from controllers.categoryWs import category_ws
from controllers.new_admin import new_admin_bp
from controllers.logout import logout_bp
from controllers.new_category import new_category_bp
from controllers.product_update import product_update_bp
from models.admins import Admins
from models.category import Category
from models.products import Products
from controllers.back_office import back_office_bp
from controllers.catalogue import catalogue_bp
from controllers.homepage import homepage_bp
from controllers.login import login_bp
from controllers.productWs import product_ws
from config.config import Config
from database.database import db
from datetime import timedelta

app = Flask(__name__)

app.config.from_object(Config)  # import la configuration de l'app

app.permanent_session_lifetime = timedelta(minutes=90)

# Import des routes Blueprint
app.register_blueprint(product_ws)
app.register_blueprint(category_ws)
app.register_blueprint(homepage_bp)
app.register_blueprint(catalogue_bp)
app.register_blueprint(login_bp)
app.register_blueprint(back_office_bp)
app.register_blueprint(product_update_bp)
app.register_blueprint(new_category_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(admin_ws)
app.register_blueprint(new_admin_bp)

db.init_app(app)

# verifie la presence des table de l'application et les créer si ce n'est pas le cas
with app.app_context():
    if not inspect(db.engine).has_table('category'):
        Category.__table__.create(bind=db.engine)

    if not inspect(db.engine).has_table('products'):
        Products.__table__.create(bind=db.engine)

    if not inspect(db.engine).has_table('admins'):
        Admins.__table__.create(bind=db.engine)

if __name__ == '__main__':
    app.run()
