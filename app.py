from flask import Flask
from sqlalchemy import inspect
from controllers.categoryWs import category_ws
from controllers.new_category import new_category_bp
from controllers.product_update import product_update_bp
from models.category import Category
from models.products import Products
from controllers.back_office import back_office_bp
from controllers.catalogue import catalogue_bp
from controllers.homepage import homepage_bp
from controllers.login import login_bp
from controllers.productWs import product_ws
from config.config import Config
from database.database import db

app = Flask(__name__)

app.config.from_object(Config)  # import la configuration de la connexion à la base de données

app.register_blueprint(product_ws)  # import le blueprint avec les routes dans 'productWs.py'
app.register_blueprint(category_ws)  # import le blueprint avec les routes dans 'categoryWs.py'
app.register_blueprint(homepage_bp)  # import le blueprint avec les routes dans 'homepage.py'
app.register_blueprint(catalogue_bp)  # import le blueprint avec les routes dans 'catalogue.py'
app.register_blueprint(login_bp)  # import le blueprint pour les routes dans 'login.py'
app.register_blueprint(back_office_bp)  # import le blueprint les routes dans 'back_office.py'
app.register_blueprint(product_update_bp)  # import le blueprint avec les routes dans 'product_update.py'
app.register_blueprint(new_category_bp) # import le blueprint avec les routes dans 'new_category.py'

db.init_app(app)

# verifie la presence des table de l'application et les créer si ce n'est pas le cas
with app.app_context():
    if not inspect(db.engine).has_table('category'):
        Category.__table__.create(bind=db.engine)

    if not inspect(db.engine).has_table('products'):
        Products.__table__.create(bind=db.engine)

if __name__ == '__main__':
    app.run()
