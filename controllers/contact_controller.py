from dao.contact_dao import ContactDao

class ContactController:
    def __init__(self, user):
        self.user = user
        self.contact_dao = ContactDao(user)
        
    def list_contacts(self, user_id):
        return self.contact_dao.list_contacts(user_id)
    
    def select_contact(self, contact_id):
        return self.contact_dao.select_contact(contact_id)
    
    def filter_conctacts(self, item):
        return self.contact_dao.filter_contacts(item)
    
    def insert_contact(self, contact):
        self.contact_dao.insert_contact(contact)
    
    def update_contact(self, contact):
        self.contact_dao.update_contact(contact)
    
    def block_contact(self, contact_id):
        self.contact_dao.block_contact(contact_id)
    
    def unblock_contact(self, contact_id):
        self.contact_dao.unblock_contact(contact_id)
    
    def delete_contact(self, contact_id):
        self.contact_dao.delete_contact(contact_id)