from app.extensions import db
from app.models.base.base_model import BaseModel

class Term(BaseModel):
  __tablename__ = "terms"

  id = db.Column(
    db.Integer, 
    primary_key = True
  )

  term_category_id = db.Column(
    db.Integer, 
    db.ForeignKey("term_categories.id"), 
    nullable = False
  )

  animation_id = db.Column(
    db.Integer, 
    db.ForeignKey("animations.id"), 
    nullable = False
  )

  text = db.Column(
    db.String(200), 
    nullable = False
  )