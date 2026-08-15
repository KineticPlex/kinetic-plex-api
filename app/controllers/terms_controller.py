from flask.views import MethodView
from flask import jsonify, request
from app.services.term_service import TermService

class TermsController(MethodView):
  
  def get(self, term_id = None):

    try:
        if term_id is None:
            terms = TermService.get_all()
            
            resultado = [{
                'id': term.id,
                'term_category_id': term.term_category_id,
                'animation_id': term.animation_id,
                'text': term.text
            } for term in terms]
            
            return jsonify(resultado), 200
        else:
            term = TermService.get_by_id(term_id)

            if not term:
                return jsonify({"error": "Term not found"}), 404
                
            return jsonify({
                'id': term.id,
                'term_category_id': term.term_category_id,
                'animation_id': term.animation_id,
                'text': term.text
            }), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def post(self):

    try:
        data = request.get_json()
        
        if not data or 'termCategoryId' not in data or 'animationId' not in data or 'text' not in data:
            return jsonify({"error": "The fields termCategoryId, animationId, and text are required"}), 400
            
        new_term = TermService.create(
            term_category_id = data.get('termCategoryId'),
            animation_id = data.get('animationId'),
            text = data.get('text')
        )
        
        return jsonify({
            "message": "Term created successfully", 
            "id": new_term.id
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def put(self, term_id):

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided for update"}), 400
            
        updated_term = TermService.update(term_id, data)
        if not updated_term:
            return jsonify({"error": "Term not found"}), 404
            
        return jsonify({
            "message": "Term updated successfully",
            "id": updated_term.id
        }), 200
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def delete(self, term_id):

    try:
        success = TermService.delete(term_id)
        
        if not success:
            return jsonify({"error": "Term not found"}), 404
            
        return jsonify({"message": "Term deleted successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500