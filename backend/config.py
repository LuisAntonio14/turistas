import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGODB_SETTINGS = {
        'db': 'turistas',
        'host': 'mongodb+srv://antonio:1@cluster0.avklr.mongodb.net/turistas?retryWrites=true&w=majority&appName=Cluster0',
        'port': 27017
    }
