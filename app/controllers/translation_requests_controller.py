from flask.views import MethodView
from flask import jsonify, request
from app.services.translation_request_service import TranslationRequestService

class TranslationRequestsController(MethodView):
  
  def get(self, request_id = None):

    try:
      if request_id is None:
        translation_requests = TranslationRequestService.get_all()
        resultado = [{
          'id': req.id,
          'text': req.text,
          'is_resolved': req.is_resolved
        } for req in translation_requests]
        
        return jsonify(resultado), 200
      else:
        req = TranslationRequestService.get_by_id(request_id)

        if not req:
          return jsonify({"error": "Translation request not found"}), 404
            
        return jsonify({
          'id': req.id,
          'text': req.text,
          'is_resolved': req.is_resolved
        }), 200
            
    except Exception as e:
      return jsonify({"error": str(e)}), 500

  def post(self):

    try:
      data = request.get_json()
      
      if not data or 'text' not in data:
        return jsonify({"error": "The text field is required"}), 400
          
      result = TranslationRequestService.create(
        text = data.get('text')
      )
      
      new_req = result['request']
      sequences_data = result['sequences']
      
      return jsonify({
        "success": True, 
        "data": sequences_data
      }), 201
        
    except ValueError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500

  def delete(self, request_id):

    try:
      success = TranslationRequestService.delete(request_id)
      if not success:
        return jsonify({"error": "Translation request not found"}), 404
          
      return jsonify({"message": "Translation request deleted successfully"}), 200
        
    except Exception as e:
      return jsonify({"error": str(e)}), 500