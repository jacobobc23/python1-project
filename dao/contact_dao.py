import sqlite3 as sql
from db.db_connection import DataBaseConnection
from models.contact import Contact
from models.user import User   

class ContactDao:
    def __init__(self, user : User):
        self.conn = DataBaseConnection()
        self.user = user
    
    def list_contacts(self, user_id):
        user_contacts = []
        try:
            cursor = self.conn.connection.cursor()
            query = 'SELECT name, last_name, phone_number, type, email, address, emergency, blocked, id FROM contacts WHERE user_id = ?'
            cursor.execute(query, (user_id,))
            
            contacts_data = cursor.fetchall()
            
            for data in contacts_data:
                name, last_name, phone_number, _type, email, address, emergency, blocked, id = data
                contact = Contact(name, last_name, phone_number, _type, email, address, emergency, blocked, id)
                user_contacts.append(contact)
            return user_contacts
        except sql.Error as err:
            print(f'Error al listar los contactos {err}')
        finally:
            cursor.close()
        
    def select_contact(self, contact_id):
        try:
            cursor = self.conn.connection.cursor()
            query = 'SELECT name, last_name, phone_number, type, email, address, emergency, blocked, id FROM contacts WHERE id = ?'
            cursor.execute(query, (contact_id,))
            
            contact_data = cursor.fetchone()
            
            if contact_data:
                name, last_name, phone_number, _type, email, address, emergency, blocked, id = contact_data
                return Contact(name, last_name, phone_number, _type, email, address, emergency, blocked, id)
        except sql.Error as err:
            print(f'Error al buscar el contacto {err}')
        finally:
            cursor.close()
            
    def filter_contacts(self, item):
        user_contacts = []
        try:
            cursor = self.conn.connection.cursor()
            query = '''SELECT name, last_name, phone_number, type, email, address, emergency, blocked, id 
                   FROM contacts
                   WHERE name LIKE ? OR last_name LIKE ? OR phone_number LIKE ? OR email LIKE ? OR address LIKE ?'''
            
            value = f'{item}%'
            values = (value, value, value, value, value)
            cursor.execute(query, values)
            
            contacts_data = cursor.fetchall()
            
            for data in contacts_data:
                name, last_name, phone_number, _type, email, address, emergency, blocked, id = data
                contact = Contact(name, last_name, phone_number, _type, email, address, emergency, blocked, id)
                user_contacts.append(contact)
            return user_contacts
        except sql.Error as err:
            print(f'Error al filtrar los contactos {err}')
        finally:
            cursor.close()
            
    def insert_contact(self, contact : Contact):
        try:
            cursor = self.conn.connection.cursor()
            query = '''INSERT INTO contacts (name, last_name, phone_number, email, address, emergency, type, blocked, user_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
            values = (contact.name, contact.last_name, contact.phone_number, contact.email, contact.address, contact.emergency, contact.type_contact, contact.blocked, self.user.id)
            cursor.execute(query, values)
            
            self.conn.connection.commit()
        except sql.Error as err:
            print(f'Error al insertar el contacto {err}')
        finally:
            cursor.close()
    
    def update_contact(self, contact : Contact):
        try:
            cursor = self.conn.connection.cursor()
            query = '''UPDATE contacts SET name = ?, last_name = ?, phone_number = ?, email = ?, address = ?, emergency = ?,
                    type = ?, blocked = ? WHERE id = ?'''
            
            values = (contact.name, contact.last_name, contact.phone_number, contact.email, contact.address, contact.emergency, contact.type_contact, contact.blocked, contact.id)
            cursor.execute(query, values)
            
            self.conn.connection.commit()
        except sql.Error as err:
            print(f'Error al actualizar el contacto {err}')
        finally:
            cursor.close()
    
    def block_contact(self, contact_id):
        try:
            cursor = self.conn.connection.cursor()
            query = 'UPDATE contacts SET blocked = 1 WHERE id = ?'
            
            cursor.execute(query, (contact_id, ))
            
            self.conn.connection.commit()
        except sql.Error as err:
            print(f'Error al bloquear el contacto {err}')
        finally:
            cursor.close()
            
    def unblock_contact(self, contact_id):
        try:
            cursor = self.conn.connection.cursor()
            query = 'UPDATE contacts SET blocked = 0 WHERE id = ?'
            
            cursor.execute(query, (contact_id, ))
            
            self.conn.connection.commit()
        except sql.Error as err:
            print(f'Error al desbloquear el contacto {err}')
        finally:
            cursor.close() 
    
    def delete_contact(self, contact_id):
        try:
            cursor = self.conn.connection.cursor()
            query = 'DELETE FROM contacts WHERE id = ?'
    
            cursor.execute(query, (contact_id, ))
    
            self.conn.connection.commit()
        except sql.Error as err:
            print(f'Error al eliminar el contacto {err}')
        finally:
            cursor.close()
            