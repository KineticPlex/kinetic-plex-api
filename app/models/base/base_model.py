from app.extensions import db

class BaseModel(db.Model):
  __abstract__  =  True

  creation_time = db.Column(
    db.DateTime, 
    default = db.func.current_timestamp()
  )
  
  last_modification_time = db.Column(
    db.DateTime, 
    nullable = True,
    onupdate = db.func.current_timestamp()
  )
  
  is_deleted = db.Column(
    db.Boolean, 
    default = False, 
    nullable = False
  )