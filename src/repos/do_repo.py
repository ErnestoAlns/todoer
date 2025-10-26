from src.models.task import TaskRegister, TaskModel
from ..models.user import UserRegister, UserModel

class UserRepo:

    def insert_user(self, connection, data: UserRegister):
        cursor = connection.cursor(dictionary=True)
        sql = 'INSERT INTO users (username, password) values (%(username)s, %(password)s)'
        try:
            cursor.execute(sql, data.model_dump())
            connection.commit()
        finally:
            cursor.close()

    def insert_task(self, connection, data: TaskRegister):
        cursor = connection.cursor(dictionary=True)
        sql = 'INSERT INTO task (created_by, titile, descTask, state) values (%(created_by)s, %(titile)s, %(descTask)s, %(state)s)'
        try: 
            cursor.execute(sql, data.model_dump())
            connection.commit()
        finally:
            cursor.close()

    def get_user_by_name(self, connection, username: str) -> UserModel | None:
        cursor = connection.cursor(dictionary=True)
        sql = 'SELECT id, username, password FROM users WHERE username = %s'
        try:
            cursor.execute(sql, [username])
            sql_user_data = cursor.fetchone()
            if sql_user_data is None:
                return None
            else: 
                user_data = UserModel.model_validate(sql_user_data)
                return user_data

        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            raise

        finally: 
            cursor.close()

    def get_task_sql(self, connection, user_id: int) -> TaskModel | None:
       cursor = connection.cursor(dictionary=True)
       sql = 'SELECT id, created_by, daydate, titile, descTask, state FROM task WHERE created_by = %s'
       cursor.execute(sql, [user_id])
       tasks_sql = cursor.fetchall()
       return tasks_sql

    def update(self, connection, id, data: TaskRegister):
        cursor = connection.cursor(dictionary=True)
        sql = 'UPDATE task SET titile = %(titile)s, descTask = %(descTask)s WHERE id = %(id)s'
        values =data.model_dump()
        values['id'] = id
        try: 
            cursor.execute(sql, values)
            connection.commit()
        finally:
            cursor.close()

    def delete(self, connection, id: int):
        cursor = connection.cursor(dictionary=True)
        sql = 'DELETE FROM task WHERE id = %s'
        try: 
            cursor.execute(sql, [int(id)])
            connection.commit()

        except Exception as e:
            print(f"Error al elminiar tarea: {e}")
            raise

        finally:
            cursor.close()

