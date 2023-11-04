from tkinter import messagebox
from controllers.contact_controller import ContactController
from models.user import User
from views_design.home import HomeDesign

class HomeWindow(HomeDesign):
    def __init__(self, user : User):
        self.user = user
        self.controller = ContactController(user)
        super().__init__()
    
    def add_contact(self):
        from views.register_contact import RegisterContactWindow
        self.window.destroy()
        RegisterContactWindow(self.user)
        
    def update_contact(self):
        item = self.table.selection()
        
        if item:
            from views.update_contact import UpdateContactWindow
            contact_id = self.table.item(item, 'text')
            contact = self.controller.select_contact(contact_id)
            self.window.destroy()
            UpdateContactWindow(self.user, contact)
        else:
            messagebox.showwarning(message='Seleccione un contacto de la tabla', title='Advertencia')
    
    def delete_contact(self):
        item = self.table.selection()
        
        if item:
            contact_id = self.table.item(item, 'text')
            self.controller.delete_contact(contact_id)
            messagebox.showinfo(message='Contacto eliminado')
            self.refresh_table()
        else:
            messagebox.showwarning(message='Seleccione un contacto', title='Advertencia')
            
    def block_contact(self):
        item = self.table.selection()
        
        if item:
            contact_id = self.table.item(item, 'text')
            self.controller.block_contact(contact_id)
            messagebox.showinfo(message='Contacto bloqueado')
            self.refresh_table()
        else:
            messagebox.showwarning(message='Seleccione un contacto', title='Advertencia')
        
    def unblock_contact(self):
        item = self.table.selection()
        
        if item:
            contact_id = self.table.item(item, 'text')
            self.controller.unblock_contact(contact_id)
            messagebox.showinfo(message='Contacto desbloqueado')
            self.refresh_table()
        else:
            messagebox.showwarning(message='Seleccione un contacto', title='Advertencia')
            
    def show_all_contacts(self):
        self.refresh_table()
    
    def search_contacts_by_filter(self):
        atr = self.filter.get()
        if atr:
            contacts = self.controller.filter_conctacts(atr)
            if contacts:
                self.fill_table(contacts)
            else:
                messagebox.showerror(message='No se encontraron resultados', title='Advertencia') 
                self.refresh_table()
        else:
            messagebox.showwarning(message='Ingrese algún dato', title='Advertencia')
    
    def refresh_table(self):
        contacts = self.controller.list_contacts(self.user.id)
        self.fill_table(contacts)