from app.extensions import db
from app.models.base.base_model import BaseModel

class TranslationRequest(BaseModel):
  
  __tablename__ = "translation_requests"

  id = db.Column(
    db.Integer, 
    primary_key = True
  )

  text = db.Column(
    db.String(500), 
    nullable = False
  )

  is_resolved = db.Column(
    db.Boolean,
    default = False,
    nullable = False
  )