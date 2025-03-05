from flask import Flask
from config import Config
from app_routes import bp as routes_bp  # Actualiza el nombre de la importación
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

db = MongoEngine()
db.init_app(app)

app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
