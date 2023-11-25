from tkinter import messagebox
from controllers.contact_controller import ContactController
from views_design.update_contact import UpdateContactDesign

class UpdateContactWindow(UpdateContactDesign):
    def __init__(self, user, contact):
        self.user = user
        self.contact = contact
        self.controller = ContactController(user)
        super().__init__(contact)
        
    def update_contact(self):
       
        try:
            self.contact.name = self.name.get()
            self.contact.last_name = self.last_name.get()
            self.contact.phone_number = int(self.phone_num.get())
            self.contact.email = self.email.get()
            self.contact.address = self.address.get()
            self.contact.type_contact = self.cbx_type.get()
            self.contact.emergency = self.emergency.get()
            
            if not self.are_valid_fields(self.name.get(), self.phone_num.get(), self.cbx_type.get()):
                messagebox.showwarning(message='Ingrese todos los datos', title='advertencia')
                return

            self.controller.update_contact(self.contact)
            messagebox.showinfo(message='Contacto actualizado correctamente')
            self.return_to_home()
        except ValueError:
            messagebox.showerror(message='Ingrese un número de teléfono válido')
            
    def return_to_home(self):
        from views.home import HomeWindow
        self.window.destroy()
        HomeWindow(self.user)    
    
    def are_valid_fields(self, name, phone_num, _type):
        return name != '' and phone_num != None and _type != 'Seleccione una opción'