from app.models.term import Term
from app.repositories.term_repository import TermRepository

class TermService:

  @staticmethod
  def get_all(include_deleted = False):

    return TermRepository.get_all(include_deleted)

  @staticmethod
  def get_by_id(term_id):

    return TermRepository.get_by_id(term_id)

  @staticmethod
  def create(term_category_id, animation_id, text):

    new_term = Term(
      term_category_id = term_category_id,
      animation_id = animation_id,
      text = text.lower().strip()
    )

    return TermRepository.create(new_term)

  @staticmethod
  def update(term_id, data):

    term = TermRepository.get_by_id(term_id)

    if not term:
      return None

    if 'term_category_id' in data:
      term.term_category_id = data['term_category_id']
    if 'animation_id' in data:
      term.animation_id = data['animation_id']
    if 'text' in data:
      term.text = data['text'].lower().strip()

    TermRepository.update()

    return term

  @staticmethod
  def delete(term_id):

    term = TermRepository.get_by_id(term_id)
    
    if not term:
      return False

    return TermRepository.delete(term)