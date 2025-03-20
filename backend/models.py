from flask_mongoengine import MongoEngine
from datetime import datetime
from mongoengine import Document, StringField, ReferenceField

# Inicializar la instancia de MongoEngine
db = MongoEngine()

# Modelo para el Usuario (Para el login)
class Usuario(db.Document):
    nombre = db.StringField(required=True)  # Nombre del usuario
    contrasena = db.StringField(required=True)  # Contraseña del usuario

# Modelo para la Locación (En este caso, las locaciones que los turistas pueden visitar)
class Locacion(db.Document):
    nombre = db.StringField(required=True)  # Nombre de la locación

# Modelo para el Turista (Para gestionar la información de los turistas)
class Turista(db.Document):
    nombre = db.StringField(required=True)  # Nombre del turista
    locacion = db.ReferenceField('Locacion', required=True)  # Referencia a la locación que visitó (Relación con el modelo Locacion)
    fecha = db.DateTimeField(default=datetime.utcnow)  # Fecha de la visita (se establece a la hora actual por defecto)
    hora = db.StringField(required=True)  # Hora en la que el turista visitó la locación
