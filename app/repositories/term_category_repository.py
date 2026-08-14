from app.extensions import db
from app.models.term_category import TermCategory

class TermCategoryRepository:

  @staticmethod
  def get_all():
    return TermCategory.query.filter_by(is_deleted = False).all()

  @staticmethod
  def get_by_id(category_id):
    return TermCategory.query.get(category_id)

  @staticmethod
  def create(name, description):
    new_category = TermCategory(name = name, description = description)

    db.session.add(new_category)
    db.session.commit()

    return     db.session.add(new_category)
