from app.models.term_category import TermCategory
from app.repositories.term_category_repository import TermCategoryRepository

class TermCategoryService:

  @staticmethod
  def get_all(include_deleted = False):

    return TermCategoryRepository.get_all(include_deleted)

  @staticmethod
  def get_by_id(category_id):

    return TermCategoryRepository.get_by_id(category_id)

  @staticmethod
  def create(name, description):

    new_category = TermCategory(
      name = name,
      description = description
    )

    return TermCategoryRepository.create(new_category)

  @staticmethod
  def update(category_id, data):

    category = TermCategoryRepository.get_by_id(category_id)
    
    if not category:
      return None

    if 'name' in data:
      category.name = data['name']
    if 'description' in data:
      category.description = data['description']

    TermCategoryRepository.update()

    return category

  @staticmethod
  def delete(category_id):

    category = TermCategoryRepository.get_by_id(category_id)
    
    if not category:
      return False

    return TermCategoryRepository.delete(category)