import uuid
from app.models.animation import Animation

class AnimationService:

    @staticmethod
    def get_all(include_deleted = False):

      query = Animation.query

      if not include_deleted:
          query = query.filter_by(is_deleted = False)
          
      return query.all()

    @staticmethod
    def get_by_id(animation_id):
        
      return Animation.query.filter_by(id = animation_id, is_deleted = False).first()

    @staticmethod
    def get_by_key(animation_key):
        
      return Animation.query.filter_by(key = animation_key, is_deleted = False).first()

    @staticmethod
    def create(name, duration, category_id = None, description = None):

      new_animation = Animation(
          category_id = category_id,
          key = str(uuid.uuid4()),
          name = name,
          duration = duration,
          description = description
      )

      db.session.add(new_animation)
      db.session.commit()

      return new_animation

    @staticmethod
    def update(animation_id, data):
      animation = AnimationService.get_by_id(animation_id)
      if not animation:
          return None

      if 'name' in data:
          animation.name = data['name']
      if 'duration' in data:
          animation.duration = data['duration']
      if 'category_id' in data:
          animation.category_id = data['category_id']
      if 'description' in data:
          animation.description = data['description']

      db.session.commit()

      return animation

    @staticmethod
    def delete(animation_id):
      animation = AnimationService.get_by_id(animation_id)

      if not animation:
          return False
      
      db.session.commit()

      return True