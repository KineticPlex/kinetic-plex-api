from app.extensions import db
from app.models.base.base_model import BaseModel

class Animation(BaseModel):
  __tablename__ = "animations"

  id = db.Column(
    db.Integer, 
    primary_key = True
  )

  term_category_id = db.Column(
    db.Integer, 
    db.ForeignKey("term_categories.id"), 
    nullable = True
  )

  key = db.Column(
    db.String(36), 
    unique = True, 
    nullable = False
  )

  name = db.Column(
    db.String(100), 
    nullable = False
  )

  duration = db.Column(
    db.Integer, 
    nullable = False
  )

  description = db.Column(
    db.String(150), 
    nullable = True
  )