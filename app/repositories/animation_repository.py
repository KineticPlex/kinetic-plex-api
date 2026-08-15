from app.extensions import db
from app.models.animation import Animation

class AnimationRepository:

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
  def create(animation):

    db.session.add(animation)
    db.session.commit()

    return animation

  @staticmethod
  def update():

    db.session.commit()

  @staticmethod
  def delete(animation):

    animation.is_deleted = True
    db.session.commit()

    return True