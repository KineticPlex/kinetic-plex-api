from app.extensions import db
from app.models.animation_sequence import AnimationSequence

class AnimationSequenceRepository:

  @staticmethod
  def get_all(include_deleted = False):
    
    query = AnimationSequence.query

    if not include_deleted:
      query = query.filter_by(is_deleted = False)

    return query.all()

  @staticmethod
  def get_by_id(record_id):
    
    return AnimationSequence.query.filter_by(id = record_id, is_deleted = False).first()

  @staticmethod
  def get_by_sequence_id(sequence_id, include_deleted = False):
    
    query = AnimationSequence.query.filter_by(sequence_id = sequence_id)

    if not include_deleted:
      query = query.filter_by(is_deleted = False)

    return query.all()

  @staticmethod
  def create(animation_sequence):

    db.session.add(animation_sequence)
    db.session.commit()

    return animation_sequence

  @staticmethod
  def update():

    db.session.commit()

  @staticmethod
  def delete(animation_sequence):

    animation_sequence.is_deleted = True
    db.session.commit()

    return True