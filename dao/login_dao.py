import sqlite3 as sql
from db.db_connection import DataBaseConnection
from exceptions.user_exceptions import CredentialsException
from models.user import User

class LoginDao:
    def __init__(self):
        self.conn = DataBaseConnection()    
        
    def select_user(self, email, password):
        try:
            cursor = self.conn.connection.cursor()
            query = 'SELECT name, email, password, id FROM users WHERE email = ? AND  password = ?'
            cursor.execute(query, (email, password))
            
            user_data = cursor.fetchone()
            
            if user_data:
                name, email, password, id = user_data
                return User(name, email, password, id)
            else:
                raise CredentialsException()
        except sql.Error as err:
            print(f'Error al buscar el usuario {err}')
        finally:
            cursor.close()
        