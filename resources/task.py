# resources/task.py

from flask import request
from flask_restful import Resource
from models import tasks

class Task(Resource):
    def get(self, task_id):
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        return task, 200

    def post(self):
        data = request.get_json()
        task_id = len(tasks) + 1
        task = {'id': task_id, 'title': data['title'], 'description': data.get('description', '')}
        tasks.append(task)
        return task, 201

    def put(self, task_id):
        data = request.get_json()
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task is None:
            return {'message': 'Task not found'}, 404
        task.update(data)
        return task, 200

    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return '', 204
