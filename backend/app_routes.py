from flask import Blueprint, request, jsonify
from models import Usuario, Locacion, Turista  # Asegúrate de importar Locacion y Turista
from bson import ObjectId

# Definir el blueprint para las rutas de la aplicación
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

# Ruta para registrar un turista
@bp.route('/registrar_turista', methods=['POST'])
def registrar_turista():
    try:
        # Obtener los datos enviados en la solicitud
        data = request.get_json()
        locacion_id = data.get('locacion_id')  # ID de la locación (ObjectId)
        hora = data.get('hora')  # Hora de la visita
        fecha = data.get('fecha')  # Fecha de la visita

        # Verificar que los datos necesarios estén presentes
        if not locacion_id or not hora or not fecha:
            return jsonify({'message': 'Datos incompletos'}), 400

        # Buscar la locación por su ID (ObjectId)
        locacion = Locacion.objects(id=locacion_id).first()

        # Si no se encuentra la locación, se devuelve un error 404
        if not locacion:
            return jsonify({'message': 'Locación no encontrada'}), 404

        # Crear un nuevo turista y asociarlo con la locación encontrada
        turista = Turista(locacion=locacion, hora=hora, fecha=fecha)
        turista.save()  # Guardar el nuevo turista en la base de datos

        # Respuesta de éxito
        return jsonify({'message': 'Turista registrado con éxito'}), 201

    except Exception as e:
        return jsonify({'message': 'Error al registrar el turista', 'error': str(e)}), 500

# Endpoints para obtener todos los turistas por locación
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

@bp.route('/test', methods=['POST'])
def test_connection():
    data = request.get_json()  # Recibir el mensaje en formato JSON
    mensaje = data.get('mensaje')
    if mensaje:
        return jsonify({'message': 'Conexión exitosa', 'received': mensaje}), 200
    else:
        return jsonify({'message': 'No se recibió mensaje'}), 400

# Endpoints para filtrar por fecha (YYYY-MM) combinando locación y fecha

# Para Santa Cruz (se mantiene el endpoint existente)
@bp.route('/turistas/filtrar_fecha', methods=['GET'])
def filtrar_por_fecha():
    fecha = request.args.get('fecha')  # Se espera un valor tipo "YYYY-MM"
    if not fecha:
        return jsonify({'message': 'Fecha no proporcionada'}), 400

    locacion = Locacion.objects(nombre="Santa Cruz").first()
    if not locacion:
        return jsonify({'message': 'Locación "Santa Cruz" no encontrada'}), 404

    try:  
        # Filtra turistas de Santa Cruz cuya fecha comience con "YYYY-MM"
        turistas = Turista.objects(locacion=locacion.id, fecha__startswith=fecha)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    except Exception as e:
        return jsonify({'message': 'Error al filtrar turistas', 'error': str(e)}), 500

# Para La Cueva
@bp.route('/turistas/filtrar_fecha_lacueva', methods=['GET'])
def filtrar_fecha_lacueva():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({'message': 'Fecha no proporcionada'}), 400

    locacion = Locacion.objects(nombre="La Cueva").first()
    if not locacion:
        return jsonify({'message': 'Locación "La Cueva" no encontrada'}), 404

    try:
        turistas = Turista.objects(locacion=locacion.id, fecha__startswith=fecha)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    except Exception as e:
        return jsonify({'message': 'Error al filtrar turistas', 'error': str(e)}), 500

# Para Presa de Malpaso
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

# Para Santuario
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
