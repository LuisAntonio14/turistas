from flask import Blueprint, request, jsonify
from models import Usuario, Locacion, Turista  # Asegúrate de importar Locacion y Turista
from bson import ObjectId

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

@bp.route('/registrar_turista', methods=['POST'])
def registrar_turista():
    try:
        data = request.get_json()
        locacion_id = data.get('locacion_id')
        hora = data.get('hora')
        fecha = data.get('fecha')

        if not locacion_id or not hora or not fecha:
            return jsonify({'message': 'Datos incompletos'}), 400

        locacion = Locacion.objects(id=locacion_id).first()

        if not locacion:
            return jsonify({'message': 'Locación no encontrada'}), 404

        turista = Turista(locacion=locacion, hora=hora, fecha=fecha)
        turista.save()
        return jsonify({'message': 'Turista registrado con éxito'}), 201

    except Exception as e:
        return jsonify({'message': 'Error al registrar el turista', 'error': str(e)}), 500

# Endpoints para obtener todos los turistas por locación (sin filtro de fecha)
@bp.route('/turistas/santa_cruz', methods=['GET'])
def turistas_santa_cruz():
    locacion = Locacion.objects(nombre="Santa Cruz").first()
    if locacion:
        turistas = Turista.objects(locacion=locacion.id)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    else:
        return jsonify({'message': 'Locación "Santa Cruz" no encontrada'}), 404

@bp.route('/turistas/lacueva', methods=['GET'])
def turistas_lacueva():
    locacion = Locacion.objects(nombre="La Cueva").first()
    if locacion:
        turistas = Turista.objects(locacion=locacion.id)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    else:
        return jsonify({'message': 'Locación "La Cueva" no encontrada'}), 404

@bp.route('/turistas/presa', methods=['GET'])
def turistas_presa():
    locacion = Locacion.objects(nombre="Presa de Malpaso").first()
    if locacion:
        turistas = Turista.objects(locacion=locacion.id)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    else:
        return jsonify({'message': 'Locación "Presa de Malpaso" no encontrada'}), 404

@bp.route('/turistas/santuario', methods=['GET'])
def turistas_santuario():
    locacion = Locacion.objects(nombre="Santuario").first()
    if locacion:
        turistas = Turista.objects(locacion=locacion.id)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    else:
        return jsonify({'message': 'Locación "Santuario" no encontrada'}), 404

# Endpoints para filtrar por fecha (YYYY-MM) y locación
@bp.route('/turistas/filtrar_fecha_lacueva', methods=['GET'])
def filtrar_fecha_lacueva():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({'message': 'Fecha no proporcionada'}), 400

    locacion = Locacion.objects(nombre="La Cueva").first()
    if not locacion:
        return jsonify({'message': 'Locación "La Cueva" no encontrada'}), 404

    try:
        # Filtra turistas de "La Cueva" cuya fecha comience con el string "YYYY-MM"
        turistas = Turista.objects(locacion=locacion.id, fecha__startswith=fecha)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    except Exception as e:
        return jsonify({'message': 'Error al filtrar turistas', 'error': str(e)}), 500

@bp.route('/turistas/filtrar_fecha_presa', methods=['GET'])
def filtrar_fecha_presa():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({'message': 'Fecha no proporcionada'}), 400

    locacion = Locacion.objects(nombre="Presa de Malpaso").first()
    if not locacion:
        return jsonify({'message': 'Locación "Presa de Malpaso" no encontrada'}), 404

    try:
        turistas = Turista.objects(locacion=locacion.id, fecha__startswith=fecha)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    except Exception as e:
        return jsonify({'message': 'Error al filtrar turistas', 'error': str(e)}), 500

@bp.route('/turistas/filtrar_fecha_santuario', methods=['GET'])
def filtrar_fecha_santuario():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({'message': 'Fecha no proporcionada'}), 400

    locacion = Locacion.objects(nombre="Santuario").first()
    if not locacion:
        return jsonify({'message': 'Locación "Santuario" no encontrada'}), 404

    try:
        turistas = Turista.objects(locacion=locacion.id, fecha__startswith=fecha)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    except Exception as e:
        return jsonify({'message': 'Error al filtrar turistas', 'error': str(e)}), 500

@bp.route('/test', methods=['POST'])
def test_connection():
    data = request.get_json()
    mensaje = data.get('mensaje')
    if mensaje:
        return jsonify({'message': 'Conexión exitosa', 'received': mensaje}), 200
    else:
        return jsonify({'message': 'No se recibió mensaje'}), 400
