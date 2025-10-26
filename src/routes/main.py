from flask import Blueprint, g, redirect, render_template, request, flash, session, url_for
from ..database.connection import get_db_connection
from ..service.main import delete_task, list_task, register_user, user_login, register_task, update_task
from ..repos.do_repo import UserRepo


user_repo = UserRepo()

todo = Blueprint('todo', __name__, url_prefix = '/todo')

@todo.before_request
def connect_db():
    if 'db_connection' not in g:
        g.db_connection = get_db_connection()

@todo.route('/')
def index():
    return render_template('pages/home.html')

@todo.route('/task', methods=['POST', 'GET'])
def task():
    connection = g.db_connection
    user_id = session['user_id']
    tasks = list_task(connection, user_id)

    if request.method == 'POST':
        task_data = request.form.to_dict()
        data = register_task(connection, user_id, task_data)
        return redirect(url_for('todo.task'))


    return render_template('pages/task.html', tasks = tasks)

@todo.route('/login', methods = ['POST', 'GET'])
def login():
    connection = g.db_connection
    if request.method == 'POST':
        user_data = request.form.to_dict()
        user_session = user_login(connection, (user_data))
        if user_session: 
            session.clear()
            session['user_id'] = user_session.id
            return redirect(url_for('todo.task'))
        else: 
            error = 'Error en registro'
            flash(error)

    return render_template('pages/login.html')

@todo.route('/signup', methods = ['POST', 'GET'])
def signup():
    connection = g.db_connection
    if request.method == 'POST':
        user_data = request.form.to_dict()
        data = register_user(connection, user_data)
        return redirect(url_for('todo.login'))

    return render_template('pages/signup.html')

@todo.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    connection = g.db_connection
    user_id = session['user_id']

    if request.method == 'POST':
        task_data = request.form.to_dict()
        data = update_task(connection, id, task_data)
        return redirect(url_for('todo.task'))

    return render_template('pages/update.html')

@todo.route('/delete/<id>')
def delete(id):
    connection = g.db_connection
    task = delete_task(connection, id)
    return redirect(url_for('todo.task'))






