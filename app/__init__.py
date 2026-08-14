from flask import Flask
from app.controllers import TextsController

def create_app():
    app = Flask(__name__)

    text_view = TextsController.as_view('text_controller')
    app.add_url_rule('/texts', view_func=text_view, methods=['GET', 'POST'])

    return app