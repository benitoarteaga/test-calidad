from flask import Blueprint, request, jsonify

from modelos.persona import Persona

persona_bp = Blueprint('personas', __name__)


@persona_bp.route('/personas', methods=['GET'])
def listar_personas():
    personas = Persona.listar()
    return jsonify([persona.to_dict() for persona in personas])


@persona_bp.route('/personas/<int:id>', methods=['GET'])
def buscar_personas(id):
    persona = Persona.buscar(id)
    if persona:
        return jsonify(persona.to_dict())
    return jsonify({"error": "Persona no encontrada"}), 404


@persona_bp.route('/personas', methods=['POST'])
def registrar_personas():
    data = request.get_json()
    nueva_persona = Persona.registrar(
        nombre=data.get('nombre'),
        apellidos=data.get('apellidos'),
        carnet_identidad=data.get('carnetIdentidad'),
        correo=data.get('correo'),
        telefono=data.get('telefono'),
        activo=data.get('activo', True)
    )
    return jsonify(nueva_persona.to_dict()), 201


@persona_bp.route('/personas/<int:id>', methods=['PUT'])
def modificar_personas(id):
    data = request.get_json()
    persona = Persona.buscar(id)
    if not persona:
        return jsonify({"error": "Persona no encontrada"}), 404

    persona.modificar(data)
    return jsonify(persona.to_dict())


@persona_bp.route('/personas/<int:id>', methods=['DELETE'])
def eliminar_personas(id):
    persona = Persona.buscar(id)
    if not persona:
        return jsonify({"error": "Persona no encontrada"}), 404

    persona.eliminar()
    return jsonify({"message": "Persona eliminada exitosamente"})
