from flask.views import MethodView
from flask import jsonify, request
from app.services.animation_service import AnimationService

class AnimationsController(MethodView):
  
  def get(self, animation_id = None):
    try:
        if animation_id is None:
            animations = AnimationService.get_all()
            
            resultado = [{
                'id': anim.id,
                'category_id': anim.category_id,
                'key': anim.key,
                'name': anim.name,
                'duration': anim.duration,
                'description': anim.description
            } for anim in animations]
            
            return jsonify(resultado), 200
        else:
            anim = AnimationService.get_by_id(animation_id)

            if not anim:
                return jsonify({"error": "Animation not found"}), 404
                
            return jsonify({
                'id': anim.id,
                'category_id': anim.category_id,
                'key': anim.key,
                'name': anim.name,
                'duration': anim.duration,
                'description': anim.description
            }), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def post(self):

    try:
        data = request.get_json()
        
        if not data or 'name' not in data or 'duration' not in data:
            return jsonify({"error": "The name and duration fields are required"}), 400
            
        new_anim = AnimationService.create(
            name = data.get('name'),
            duration = data.get('duration'),
            category_id = data.get('category_id'),
            description = data.get('description')
        )
        
        return jsonify({
            "message": "Animation created successfully", 
            "id": new_anim.id
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def put(self, animation_id):

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided for update"}), 400
            
        updated_anim = AnimationService.update(animation_id, data)
        if not updated_anim:
            return jsonify({"error": "Animation not found"}), 404
            
        return jsonify({
            "message": "Animation updated successfully",
            "id": updated_anim.id
        }), 200
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

  def delete(self, animation_id):

    try:
        success = AnimationService.delete(animation_id)
        if not success:
            return jsonify({"error": "Animation not found"}), 404
            
        return jsonify({"message": "Animation deleted successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500