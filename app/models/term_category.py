from app.extensions import db
from app.models.base.base_model import BaseModel

class TermCategory(BaseModel):
  __tablename__ = "term_categories"

  id = db.Column(
    db.Integer, 
    primary_key = True
  )

  name = db.Column(
    db.String(50), 
    nullable = False
  )

  description = db.Column(
    db.String(300), 
    nullable = False
  )

