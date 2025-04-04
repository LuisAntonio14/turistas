from flask import Blueprint, request, jsonify
from models import Usuario, Locacion, Turista  # Asegúrate de importar Locacion y Turista
from bson import ObjectId

bp = Blueprint('routes', __name__)

# ... (otros endpoints como login y registrar_turista)

# --- Endpoints para obtener todos los turistas sin filtro de fecha ---
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

# --- Endpoints para filtrar por fecha (YYYY-MM) combinando locación y fecha ---
# Para Cruz (Santa Cruz) usaremos el endpoint que ya tenías:
@bp.route('/turistas/filtrar_fecha', methods=['GET'])
def filtrar_fecha_cruz():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({'message': 'Fecha no proporcionada'}), 400

    locacion = Locacion.objects(nombre="Santa Cruz").first()
    if not locacion:
        return jsonify({'message': 'Locación "Santa Cruz" no encontrada'}), 404

    try:
        turistas = Turista.objects(locacion=locacion.id, fecha__startswith=fecha)
        turistas_list = [{"id": str(turista.id), "hora": turista.hora, "fecha": turista.fecha} for turista in turistas]
        return jsonify(turistas_list), 200
    except Exception as e:
        return jsonify({'message': 'Error al filtrar turistas', 'error': str(e)}), 500

# Para La Cueva:
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

# Para Presa de Malpaso:
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

# Para Santuario:
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
