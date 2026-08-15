from app.extensions import db
from app.models.base.base_model import BaseModel

class AnimationSequence(BaseModel):
  
  __tablename__ = "animations_sequences"

  id = db.Column(
    db.Integer, 
    primary_key = True
  )

  animation_id = db.Column(
    db.Integer,
    db.ForeignKey('animations.id'),
    nullable = False
  )

  sequence_id = db.Column(
    db.Integer,
    db.ForeignKey('sequences.id'),
    nullable = False
  )