from flask import Blueprint, request, jsonify
from models import Usuario, Locacion, Turista  # Asegúrate de importar Locacion y Turista

# Definir el blueprint para las rutas de la aplicación
bp = Blueprint('routes', __name__)

# Ruta para registrar un turista
@bp.route('/registrar_turista', methods=['POST'])
def registrar_turista():
    # Obtener los datos enviados en la solicitud
    data = request.get_json()
    locacion_id = data.get('locacion_id')  # ID de la locación (ObjectId)
    hora = data.get('hora')  # Hora de la visita

    # Buscar la locación por su ID (ObjectId)
    locacion = Locacion.objects(id=locacion_id).first()

    # Si no se encuentra la locación, se devuelve un error 404
    if not locacion:
        return jsonify({'message': 'Locación no encontrada'}), 404
    
    # Crear un nuevo turista y asociarlo con la locación encontrada
    turista = Turista(locacion=locacion, hora=hora)
    turista.save()  # Guardar el nuevo turista en la base de datos

    # Respuesta de éxito
    return jsonify({'message': 'Turista registrado con éxito'}), 201

# Ruta para obtener todos los turistas que visitaron "Santa Cruz"
@bp.route('/turistas/santa_cruz', methods=['GET'])
def turistas_santa_cruz():
    # Buscar la locación con el nombre "Santa Cruz"
    locacion = Locacion.objects(nombre="Santa Cruz").first()

    # Si se encuentra la locación
    if locacion:
        # Obtener todos los turistas asociados con esa locación
        turistas = Turista.objects(locacion=locacion.id)

        # Crear una lista con los datos de los turistas encontrados
        turistas_list = [{"id": str(turista.id), "hora": turista.hora} for turista in turistas]

        # Responder con la lista de turistas
        return jsonify(turistas_list), 200
    else:
        # Si la locación "Santa Cruz" no se encuentra, devolver error 404
        return jsonify({'message': 'Locación "Santa Cruz" no encontrada'}), 404
