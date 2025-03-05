import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://antonio:1@cluster0.avklr.mongodb.net/turistas?retryWrites=true&w=majority&appName=Cluster0'
    MONGODB_SETTINGS = {
        'db': 'turistas',
        'host': MONGO_URI,
        'port': 27017
    }
