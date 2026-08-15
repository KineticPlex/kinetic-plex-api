import os
from flask import Flask
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from app.extensions import db, migrate
from app.controllers.term_categories_controller import TermCategoriesController

app = Flask(__name__)

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

root_uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}"
temp_engine = create_engine(root_uri)

with temp_engine.connect() as connection:
	connection.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;"))
	connection.commit()

app.config['SQLALCHEMY_DATABASE_URI'] = f"{root_uri}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

term_categories_controller = TermCategoriesController.as_view('text_controller')
app.add_url_rule('/termCategories', view_func = term_categories_controller, methods=['GET', 'POST'])

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port = 5000)