from mysql.connector import Error
from .hashing import hash_passw, passw_auth
from ..repos.do_repo import UserRepo
from ..models.user import UserModel, UserRegister
from ..models.task import TaskModel, TaskRegister

user_repo = UserRepo()

def register_user(connection, user_data):
    password_hash = hash_passw(user_data['password'])
    user_data['password'] = password_hash
    validate_data = UserRegister.model_validate(user_data)
    user_in_sql = user_repo.get_user_by_name(connection,validate_data.username)

    error = None
    if user_in_sql is None:
        error = 'Usario {}, se encuentra registrado.'.format(user_data['username'])

    if error is None:
        data = user_repo.insert_user(connection, validate_data)
        return data
    else:
        return error

def user_login(connection, user_data) -> UserModel | None:
    validate_data = UserRegister.model_validate(user_data)
    user_in_sql = user_repo.get_user_by_name(connection, validate_data.username)

    if user_in_sql is None:
        return None

    auth = passw_auth(validate_data.password, user_in_sql.password)

    if auth is True: 
        return user_in_sql
    else: 
        return None

def register_task(connection, user_id: int, task_data):
    task_data['created_by'] = user_id
    task_data['state'] = False
    return task_data

def list_task(connection, user_id:int,):
     task_data = user_repo.get_task_sql(connection, user_id)
     return task_data

def update_task(connection, id: int, task_data):
    task_data['created_by'] = 23
    task_data['state'] = False
    validate_task = TaskRegister.model_validate(task_data)
    updated_data = user_repo.update(connection, id, validate_task)
    return updated_data

def delete_task(connection, id: int):
    task_data = user_repo.delete(connection, id)
    return task_data








