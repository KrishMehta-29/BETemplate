import mongoengine as me  # Use direct import

class User(me.Document):
    name = me.StringField(required=True)
    email = me.StringField(required=True, unique=True)
    age = me.IntField()