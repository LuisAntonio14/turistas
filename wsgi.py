import sys
import os

# Añade la ruta del directorio 'backend' al path del sistema
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from app import app

if __name__ == "__main__":
    app.run()
