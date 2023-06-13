from flask import jsonify, request, session, jsonify
from app.main import main, crud
from app.helpers.security import Security

# TYPES

@main.route('/types')
def types():
    return jsonify(crud.get_types())

@main.route('/types', methods=['POST'])
def create_type():
    return jsonify(crud.add_type(request.json))

@main.route('/types/<int:id>', methods=['PATCH'])
def update_type(id: int):
    data = request.form.to_dict()
    return jsonify(crud.change_type(id, data))

@main.route('/types/<int:id>', methods=['DELETE'])
def delete_type(id: int):
    return jsonify(crud.remove_type(id))

# TASKS

@main.route('/types', methods=['POST'])
def create_task():
    data = request.form.to_dict()
    return jsonify(crud.add_task(data))

@main.route('/tasks/<int:id>', methods=['PATCH'])
def update_task(id: int):
    data = request.form.to_dict()
    return jsonify(crud.change_task(id, data))

@main.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id: int):
    return jsonify(crud.remove_task(id))