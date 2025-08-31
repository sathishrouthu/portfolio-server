from flask import Blueprint, request, jsonify
from app.models.Task import Task

todo_bp = Blueprint('todos', __name__)


# Fetch all tasks
@todo_bp.route('/api/todos', methods=['GET'])
def get_all_tasks():
    tasks = Task.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks]), 200


# Add a new task
@todo_bp.route('/api/todos', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get("task")

    if not task:
        return jsonify({"error": "Task description is required"}), 400

    new_task = Task.add_task(task)
    return jsonify(new_task.to_dict()), 201


# Fetch task by ID
@todo_bp.route('/api/todos/<int:id>', methods=['GET'])
def get_task_by_id(id):
    task = Task.get_task_by_id(id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404


# Update a task by ID
@todo_bp.route('/api/todos/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    updated_task = Task.update_task(id, data)
    if updated_task:
        return jsonify(updated_task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404


# Delete a task by ID
@todo_bp.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_task(id):
    result = Task.delete_task(id)
    return jsonify(result), 200
