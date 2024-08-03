# app.py

from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from resources.task import Task

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

users = [{'username': 'user1', 'password': 'password1'}]

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = next((user for user in users if user['username'] == data['username'] and user['password'] == data['password']), None)
    if user is None:
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=user['username'])
    return jsonify(access_token=access_token), 200

api.add_resource(Task, '/task', '/task/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)
