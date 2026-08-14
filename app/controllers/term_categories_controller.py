from flask.views import MethodView
from flask import jsonify, request
from app.services.term_category_service import TermCategoryService

class TermCategoriesController(MethodView):
  
  def get(self):
    try:
        resultado = TermCategoryService.get_all_categories()
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def post(self):
    try:
        data = request.get_json()
        new = TermCategoryService.create_category(data)
        
        return jsonify({
            "mensaje": "Categoría creada exitosamente", 
            "id": new.id
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500