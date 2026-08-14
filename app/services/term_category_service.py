from app.repositories.term_category_repository import TermCategoryRepository

class TermCategoryService:

	@staticmethod
	def get_all_categories():
		categories  =  TermCategoryRepository.get_all()

		return [
			{
				"id": cat.id, 
				"name": cat.name, 
				"description": cat.description,
				"creation_time": cat.creation_time.isoformat() if cat.creation_time else None
			} 
			for cat in categories
		]

	@staticmethod
	def create_category(data):
		name  =  data.get('name')
		description  =  data.get('description')

		if not name or not name.strip():
			raise ValueError("El nombre de la categoría es obligatorio.")

		if not description:
			raise ValueError("La descripción es obligatoria.")

		new_category  =  TermCategoryRepository.create(name = name, description = description)

		return new_category