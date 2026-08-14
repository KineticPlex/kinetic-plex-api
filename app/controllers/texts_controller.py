from flask.views import MethodView
from flask import jsonify, request

class TextsController(MethodView):
  def get(self):
        return jsonify({
            "mensaje": "Has hecho una petición GET", 
            "texto": "¡Hola desde el controlador!"
        })

def post(self):
    data = request.get_json()
    
    return jsonify({
        "mensaje": "Has hecho una petición POST", 
        "datos_recibidos": data
    })