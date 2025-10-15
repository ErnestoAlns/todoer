from flask import Blueprint, render_template, request, url_for
from ..models.user import UserModel, UserCreate

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
        dat = request.form.to_dict()
        data = UserModel.model_validate(dat)

        return render_template('pages/test.html', data = data)
    return render_template('pages/signup.html')


