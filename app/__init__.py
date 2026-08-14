from flask import Flask
from app.extensions import db, migrate
from app.controllers.term_categories_controller import TermCategoriesController

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tu_password@localhost/kinetic_plex_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    text_view = TermCategoriesController.as_view('term_categories_controller')
    app.add_url_rule('/termCategories', view_func=text_view, methods=['GET', 'POST'])

    return app