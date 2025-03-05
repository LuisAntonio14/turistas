from flask import Blueprint, request, jsonify
from models import Usuario

bp = Blueprint('routes', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    user = Usuario.objects(nombre=nombre, contrasena=contrasena).first()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
