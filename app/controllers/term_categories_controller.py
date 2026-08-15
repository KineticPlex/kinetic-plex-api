from flask.views import MethodView
from flask import jsonify, request
from app.services.term_category_service import TermCategoryService

class TermCategoriesController(MethodView):

  def get(self, category_id = None):

    try:
      if category_id is None:
        categories = TermCategoryService.get_all()
        
        resultado = [{
          'id': cat.id,
          'name': cat.name,
          'description': cat.description
        } for cat in categories]
        
        return jsonify(resultado), 200
      else:
        cat = TermCategoryService.get_by_id(category_id)

        if not cat:
          return jsonify({"error": "Category not found"}), 404
          
        return jsonify({
          'id': cat.id,
          'name': cat.name,
          'description': cat.description
        }), 200
        
    except Exception as e:
      return jsonify({"error": str(e)}), 500

  def post(self):

    try:
      data = request.get_json()
      
      if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "The name and description fields are required"}), 400
        
      new_cat = TermCategoryService.create(
        name = data.get('name'),
        description = data.get('description')
      )
      
      return jsonify({
        "message": "Category created successfully", 
        "id": new_cat.id
      }), 201
      
    except ValueError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500

  def put(self, category_id):

    try:
      data = request.get_json()
      if not data:
        return jsonify({"error": "No data provided for update"}), 400
        
      updated_cat = TermCategoryService.update(category_id, data)

      if not updated_cat:
        return jsonify({"error": "Category not found"}), 404
        
      return jsonify({
        "message": "Category updated successfully",
        "id": updated_cat.id
      }), 200
      
    except ValueError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500

  def delete(self, category_id):

    try:
      success = TermCategoryService.delete(category_id)

      if not success:
        return jsonify({"error": "Category not found"}), 404
        
      return jsonify({"message": "Category deleted successfully"}), 200
      
    except Exception as e:
      return jsonify({"error": str(e)}), 500