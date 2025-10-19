from ..models.user import UserRegister, UserModel

class UserRepo:

    def InsertUser(self,connection, passw_hash:str,  username:str):
            cursor = connection.cursor(dictiorary=True)
#            sql = 'INSERT INTO users (username, password) values ( %(username)s, %(password)s )'
            sql = 'INSERT INTO users (username, password) values ( %s, %s )'
            values = [username, passw_hash]
            try:
                cursor.execute(sql, values)

            finally:
                cursor.close()



    def GetUser(self, connection, username: str) -> UserModel | None:
        cursor = connection.cursor(dictionary=True)
        sql = 'SELECT id, username, password FROM users WHERE username = %s'
        try:
            cursor.execute(sql, [username])
            SqlUserData = cursor.fetchone()

            if SqlUserData is None:
                return None
            NewUser = UserModel.model_validate(SqlUserData)
            return NewUser

        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            raise

        finally: 
            cursor.close()

