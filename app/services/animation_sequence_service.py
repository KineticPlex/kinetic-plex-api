from app.models.animation_sequence import AnimationSequence
from app.repositories.animation_sequence_repository import AnimationSequenceRepository

class AnimationSequenceService:

  @staticmethod
  def get_all(include_deleted = False):

    return AnimationSequenceRepository.get_all(include_deleted)

  @staticmethod
  def get_by_id(record_id):

    return AnimationSequenceRepository.get_by_id(record_id)

  @staticmethod
  def get_by_sequence_id(sequence_id):

    return AnimationSequenceRepository.get_by_sequence_id(sequence_id)

  @staticmethod
  def create(animation_id, sequence_id):

    new_record = AnimationSequence(
      animation_id = animation_id,
      sequence_id = sequence_id
    )

    return AnimationSequenceRepository.create(new_record)

  @staticmethod
  def update(record_id, data):

    record = AnimationSequenceRepository.get_by_id(record_id)
    if not record:
      return None

    if 'animation_id' in data:
      record.animation_id = data['animation_id']
    if 'sequence_id' in data:
      record.sequence_id = data['sequence_id']

    AnimationSequenceRepository.update()

    return record

  @staticmethod
  def delete(record_id):

    record = AnimationSequenceRepository.get_by_id(record_id)
    if not record:
      return False

    return AnimationSequenceRepository.delete(record)