from flask.views import MethodView
from flask import jsonify, request
from app.services.sequence_service import SequenceService

class SequencesController(MethodView):
  
  def get(self, sequence_id = None):

    try:
        if sequence_id is None:
            sequences = SequenceService.get_all()

            resultado = [{
                'id': seq.id,
                'translation_request_id': seq.translation_request_id,
                'text': seq.text,
                'order': seq.order,
                'is_resolved': seq.is_resolved
            } for seq in sequences]
            
            return jsonify(resultado), 200
        else:
            seq = SequenceService.get_by_id(sequence_id)

            if not seq:
                return jsonify({"error": "Sequence not found"}), 404
                
            return jsonify({
                'id': seq.id,
                'translation_request_id': seq.translation_request_id,
                'text': seq.text,
                'order': seq.order,
                'is_resolved': seq.is_resolved
            }), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def post(self):

    try:
        data = request.get_json()
        
        if not data or 'translation_request_id' not in data or 'text' not in data or 'order' not in data:
            return jsonify({"error": "The fields translation_request_id, text, and order are required"}), 400
            
        is_resolved = data.get('is_resolved', False)
            
        new_seq = SequenceService.create(
            translation_request_id = data.get('translation_request_id'),
            text = data.get('text'),
            order = data.get('order'),
            is_resolved = is_resolved
        )
        
        return jsonify({
            "message": "Sequence created successfully", 
            "id": new_seq.id
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def put(self, sequence_id):

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided for update"}), 400
            
        updated_seq = SequenceService.update(sequence_id, data)
        if not updated_seq:
            return jsonify({"error": "Sequence not found"}), 404
            
        return jsonify({
            "message": "Sequence updated successfully",
            "id": updated_seq.id
        }), 200
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def delete(self, sequence_id):

    try:
        success = SequenceService.delete(sequence_id)
        
        if not success:
            return jsonify({"error": "Sequence not found"}), 404
            
        return jsonify({"message": "Sequence deleted successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500