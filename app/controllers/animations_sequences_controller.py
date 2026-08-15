from flask.views import MethodView
from flask import jsonify, request
from app.services.animation_sequence_service import AnimationSequenceService

class AnimationsSequencesController(MethodView):
  
  def get(self, record_id = None):

    try:
        if record_id is None:
            records = AnimationSequenceService.get_all()

            resultado = [{
                'id': record.id,
                'animation_id': record.animation_id,
                'sequence_id': record.sequence_id
            } for record in records]
            
            return jsonify(resultado), 200
        else:
            record = AnimationSequenceService.get_by_id(record_id)

            if not record:
                return jsonify({"error": "Animation sequence not found"}), 404
                
            return jsonify({
                'id': record.id,
                'animation_id': record.animation_id,
                'sequence_id': record.sequence_id
            }), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def post(self):

    try:
        data = request.get_json()
        
        if not data or 'animation_id' not in data or 'sequence_id' not in data:
            return jsonify({"error": "The fields animation_id and sequence_id are required"}), 400
            
        new_record = AnimationSequenceService.create(
            animation_id = data.get('animation_id'),
            sequence_id = data.get('sequence_id')
        )
        
        return jsonify({
            "message": "Animation sequence created successfully", 
            "id": new_record.id
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def put(self, record_id):

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided for update"}), 400
            
        updated_record = AnimationSequenceService.update(record_id, data)
        if not updated_record:
            return jsonify({"error": "Animation sequence not found"}), 404
            
        return jsonify({
            "message": "Animation sequence updated successfully",
            "id": updated_record.id
        }), 200
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def delete(self, record_id):

    try:
        success = AnimationSequenceService.delete(record_id)
        
        if not success:
            return jsonify({"error": "Animation sequence not found"}), 404
            
        return jsonify({"message": "Animation sequence deleted successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500