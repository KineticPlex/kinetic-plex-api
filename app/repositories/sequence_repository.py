from app.extensions import db
from app.models.sequence import Sequence

class SequenceRepository:

  @staticmethod
  def get_all(include_deleted = False):
    
    query = Sequence.query

    if not include_deleted:
      query = query.filter_by(is_deleted = False)

    return query.all()

  @staticmethod
  def get_by_id(sequence_id):
    
    return Sequence.query.filter_by(id = sequence_id, is_deleted = False).first()

  @staticmethod
  def get_by_request_id(request_id, include_deleted = False):
    
    query = Sequence.query.filter_by(translation_request_id = request_id)

    if not include_deleted:
      query = query.filter_by(is_deleted = False)

    return query.order_by(Sequence.order.asc()).all()

  @staticmethod
  def create(sequence):

    db.session.add(sequence)
    db.session.commit()

    return sequence

  @staticmethod
  def update():

    db.session.commit()

  @staticmethod
  def delete(sequence):

    sequence.is_deleted = True
    db.session.commit()

    return True