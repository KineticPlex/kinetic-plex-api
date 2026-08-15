import uuid
from app.models.animation import Animation
from app.repositories.animation_repository import AnimationRepository

class AnimationService:

  @staticmethod
  def get_all(include_deleted = False):

    return AnimationRepository.get_all(include_deleted)

  @staticmethod
  def get_by_id(animation_id):

    return AnimationRepository.get_by_id(animation_id)

  @staticmethod
  def create(name, duration, category_id = None, description = None):

    new_animation = Animation(
      term_category_id = category_id,
      key = str(uuid.uuid4()),
      name = name,
      duration = duration,
      description = description
    )

    return AnimationRepository.create(new_animation)

  @staticmethod
  def update(animation_id, data):

    animation = AnimationRepository.get_by_id(animation_id)

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

    AnimationRepository.update()

    return animation

  @staticmethod
  def delete(animation_id):

    animation = AnimationRepository.get_by_id(animation_id)
    
    if not animation:
      return False
      
    return AnimationRepository.delete(animation)