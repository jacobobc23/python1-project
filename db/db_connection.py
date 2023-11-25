import sqlite3 as sql

class DataBaseConnection:
    def __init__(self):
        self.connection = self.create_connection()
    
    def create_connection(self):
        try:
            connection = sql.connect('agenda.db')
            return connection
        except sql.Error as err:
            print(f'Error al crear la conexión a la db: {err}')
            
    def close_connection(self):
        if self.connection:
            self.connection.close()