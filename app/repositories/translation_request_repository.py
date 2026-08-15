from app.extensions import db
from app.models.translation_request import TranslationRequest

class TranslationRequestRepository:

  @staticmethod
  def get_all(include_deleted = False):
    
    query = TranslationRequest.query

    if not include_deleted:
      query = query.filter_by(is_deleted = False)

    return query.all()

  @staticmethod
  def get_by_id(request_id):
    
    return TranslationRequest.query.filter_by(id = request_id, is_deleted = False).first()

  @staticmethod
  def create(translation_request):

    db.session.add(translation_request)
    db.session.commit()

    return translation_request

  @staticmethod
  def update():

    db.session.commit()

  @staticmethod
  def delete(translation_request):

    translation_request.is_deleted = True
    db.session.commit()

    return True