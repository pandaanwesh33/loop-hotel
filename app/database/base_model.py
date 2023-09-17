from peewee import Model
from database.db_session import db

class BaseModel(Model):
    class Meta:
        database = db
        only_save_dirty = True