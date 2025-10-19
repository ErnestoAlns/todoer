from flask import Blueprint, g, render_template, request, url_for
from ..models.user import UserRegister, UserModel
from ..database.connection import connection, close
from ..service.hashing import hash_passw 

todo = Blueprint('todo', __name__, url_prefix = '/todo')

@todo.route('/')
def index():
    return render_template('pages/home.html')

@todo.route('/task')
def task():
    return render_template('pages/task.html')

@todo.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('pages/login.html')

@todo.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        da = request.form.to_dict()
        password_hash = hash_passw(da['password'])
        da['password'] = password_hash
        data = UserRegister.model_validate(da)
        return render_template('pages/test.html', data = data)

    return render_template('pages/signup.html')


