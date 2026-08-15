from app.extensions import db
from app.models.base.base_model import BaseModel

class Sequence(BaseModel):
  
  __tablename__ = "sequences"

  id = db.Column(
    db.Integer, 
    primary_key = True
  )

  translation_request_id = db.Column(
    db.Integer,
    db.ForeignKey('translation_requests.id'),
    nullable = False
  )

  text = db.Column(
    db.String(100),
    nullable = False
  )

  order = db.Column(
    db.Integer,
    nullable = False
  )

  is_resolved = db.Column(
    db.Boolean,
    default = False,
    nullable = False
  )