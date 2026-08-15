from app.models.term import Term

class TermService:

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
    def create(term_category_id, animation_id, text):

        new_term = Term(
            term_category_id = term_category_id,
            animation_id = animation_id,
            text = text.lower().strip()
        )

        db.session.add(new_term)
        db.session.commit()
        
        return new_term

    @staticmethod
    def update(term_id, data):

      term = TermService.get_by_id(term_id)
      if not term:
          return None

      if 'term_category_id' in data:
          term.term_category_id = data['term_category_id']
      if 'animation_id' in data:
          term.animation_id = data['animation_id']
      if 'text' in data:
          term.text = data['text'].lower().strip()

      db.session.commit()

      return term

    @staticmethod
    def delete(term_id):

      term = TermService.get_by_id(term_id)

      if not term:
          return False
      
      term.is_deleted = True
      db.session.commit()

      return True