import datetime
from peewee import *
from app import db

# A Peewee model idiom--define a base model
# class that specifies the database to use.
class BaseModel(Model):
    class Meta:
        database = db

class Tag(BaseModel):
    name = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def __unicode__(self):
        return self.name
