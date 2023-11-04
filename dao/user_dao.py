import sqlite3 as sql
from db.db_connection import DataBaseConnection
from exceptions.user_exceptions import UserAlreadyRegisteredException
from models.user import User

class UserDao:
    def __init__(self):
        self.conn = DataBaseConnection()
        
    def select_user(self, email):
        try:
            cursor = self.conn.connection.cursor()
            query = 'SELECT name, email, password FROM users WHERE email = ?'
            cursor.execute(query, (email,))
            
            user_data = cursor.fetchone()
            
            if user_data:
                name, email, password = user_data
                return User(name, email, password)
        except sql.Error as err:
            print(f'Error al buscar el usuario {err}')
        finally:
            cursor.close()
    
    def insert_user(self, user : User):
        if self.select_user(user.email):
            raise UserAlreadyRegisteredException()
        
        try:
            cursor = self.conn.connection.cursor()
            query = 'INSERT INTO users (name, email, password) VALUES (?, ?, ?)'
            
            values = (user.name, user.email, user.password)
            cursor.execute(query, values)
            
            self.conn.connection.commit()
        except sql.Error as err:
            print(f'Error al insertar el usuario {err}')
        finally:
            cursor.close()