from flask import Blueprint, jsonify, request
from flask.views import MethodView
from flask_login import login_required, current_user

from backend.models import Todo, db


bp = Blueprint('todo', __name__)


@bp.route('/todos')
@login_required
def get_todos():
    return jsonify([todo.to_json() for todo in current_user.todos])


class TodoView(MethodView):

    def post(self):
        todo = Todo(**request.get_json())
        todo.user = current_user
        db.session.add(todo)
        db.session.commit()
        return jsonify({'status': 'success', 'todo': todo.to_json()})

    def put(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        data = request.get_json()
        for k, v in data.items():
            setattr(todo, k, v)
        db.session.commit()
        return jsonify({'status': 'success', 'todo': todo.to_json()})

    def delete(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'status': 'success'})

todo_api = login_required(TodoView.as_view('todo'))
bp.add_url_rule('/todo', view_func=todo_api, methods=['POST'])
bp.add_url_rule('/todo/<int:todo_id>', view_func=todo_api, methods=['PUT', 'DELETE'])
