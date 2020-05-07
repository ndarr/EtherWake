from peewee import SqliteDatabase, TextField, DateTimeField, BooleanField, Model
import datetime 

db = SqliteDatabase("etherwake.db")

class BaseModel(Model):
    class Meta:
        database = db

class Device(BaseModel):
    mac = TextField(index=True, unique=True, primary_key=True)
    name = TextField()
    last_checked = DateTimeField(default=datetime.datetime.now())
    online = BooleanField(default=False)

    def __get_state__(self):
        return self.__data__.items


db.create_tables([Device])
