from app.models.sequence import Sequence
from app.repositories.sequence_repository import SequenceRepository

class SequenceService:

  @staticmethod
  def get_all(include_deleted = False):

    return SequenceRepository.get_all(include_deleted)

  @staticmethod
  def get_by_id(sequence_id):

    return SequenceRepository.get_by_id(sequence_id)

  @staticmethod
  def get_by_request_id(request_id, include_deleted = False):

    return SequenceRepository.get_by_request_id(request_id, include_deleted)

  @staticmethod
  def create(translation_request_id, text, order, is_resolved):

    new_sequence = Sequence(
      translation_request_id = translation_request_id,
      text = text,
      order = order,
      is_resolved = is_resolved
    )

    return SequenceRepository.create(new_sequence)

  @staticmethod
  def update(sequence_id, data):

    sequence = SequenceRepository.get_by_id(sequence_id)
    if not sequence:
      return None

    if 'translation_request_id' in data:
      sequence.translation_request_id = data['translation_request_id']
    if 'text' in data:
      sequence.text = data['text']
    if 'order' in data:
      sequence.order = data['order']
    if 'is_resolved' in data:
      sequence.is_resolved = data['is_resolved']

    SequenceRepository.update()

    return sequence

  @staticmethod
  def delete(sequence_id):

    sequence = SequenceRepository.get_by_id(sequence_id)
    if not sequence:
      return False

    return SequenceRepository.delete(sequence)