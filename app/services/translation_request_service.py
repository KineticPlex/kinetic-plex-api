from app.models.translation_request import TranslationRequest
from app.repositories.translation_request_repository import TranslationRequestRepository
from app.models.sequence import Sequence
from app.repositories.sequence_repository import SequenceRepository
from app.repositories.term_repository import TermRepository
from app.models.animation_sequence import AnimationSequence
from app.repositories.animation_sequence_repository import AnimationSequenceRepository
from app.repositories.animation_repository import AnimationRepository
from app.services.nlp_service import NlpService

class TranslationRequestService:

  @staticmethod
  def get_all(include_deleted = False):

    return TranslationRequestRepository.get_all(include_deleted)

  @staticmethod
  def get_by_id(request_id):

    return TranslationRequestRepository.get_by_id(request_id)

  @staticmethod
  def create(text):

    new_request = TranslationRequest(
      text = text,
      is_resolved = True
    )

    created_request = TranslationRequestRepository.create(new_request)

    words = NlpService.text_to_gloss(text)
    
    all_resolved = True
    generated_sequences = []

    for index, word in enumerate(words):
      clean_word = word.strip()

      term = TermRepository.get_by_text(clean_word)
      is_word_resolved = term is not None

      if not is_word_resolved:
        all_resolved = False

      new_sequence = Sequence(
        translation_request_id = created_request.id,
        text = clean_word,
        order = index + 1,
        is_resolved = is_word_resolved
      )

      created_sequence = SequenceRepository.create(new_sequence)
      
      seq_data = {
        "order": created_sequence.order,
        "text": created_sequence.text,
        "isResolved": created_sequence.is_resolved,
        "animationKey": None,
        "animationName": None,
        "duration": None
      }

      if is_word_resolved:
        new_animation_sequence = AnimationSequence(
          animation_id = term.animation_id,
          sequence_id = created_sequence.id
        )
        
        AnimationSequenceRepository.create(new_animation_sequence)

        animation = AnimationRepository.get_by_id(term.animation_id)

        if animation:
          seq_data["animationKey"] = animation.key
          seq_data["animationName"] = animation.description
          seq_data["duration"] = animation.duration

      generated_sequences.append(seq_data)

    if not all_resolved:
      created_request.is_resolved = False
      TranslationRequestRepository.update()

    return {
      "request": created_request,
      "sequences": generated_sequences
    }

  @staticmethod
  def delete(request_id):

    translation_request = TranslationRequestRepository.get_by_id(request_id)
    if not translation_request:
      return False

    return TranslationRequestRepository.delete(translation_request)