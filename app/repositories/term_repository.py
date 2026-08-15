from app.extensions import db
from app.models.term import Term

class TermRepository:

  @staticmethod
  def get_all(include_deleted = False):
    
    query = Term.query
    if not include_deleted:
      query = query.filter_by(is_deleted = False)

    return query.all()

  @staticmethod
  def get_by_id(term_id):
    
    return Term.query.filter_by(id = term_id, is_deleted = False).first()

  @staticmethod
  def create(term):

    db.session.add(term)
    db.session.commit()

    return term

  @staticmethod
  def update():

    db.session.commit()

  @staticmethod
  def delete(term):

    term.is_deleted = True
    db.session.commit()

    return True