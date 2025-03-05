from flask_mongoengine import MongoEngine

db = MongoEngine()

class Usuario(db.Document):
    nombre = db.StringField(required=True)
    contrasena = db.StringField(required=True)
