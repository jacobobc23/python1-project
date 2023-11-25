from db.db_connection import DataBaseConnection

conn = DataBaseConnection()

USERS_TABLE = '''CREATE TABLE IF NOT EXISTS users(
                    
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                
                );'''
                
CONTACTS_TABLE = '''CREATE TABLE IF NOT EXISTS contacts(
                    
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    last_name TEXT,
                    phone_number TEXT NOT NULL,
                    email TEXT,
                    address TEXT,
                    emergency BOOLEAN,
                    type TEXT,
                    blocked BOOLEAN, 
                    user_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                
                );'''                

cursor = conn.connection.cursor()
cursor.execute(USERS_TABLE)
cursor.execute(CONTACTS_TABLE)
conn.connection.commit()

conn.close_connection()