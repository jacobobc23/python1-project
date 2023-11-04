from tkinter import messagebox
from controllers.contact_controller import ContactController
from models.contact import Contact
from views_design.register_contact import RegisterContactDesign

class RegisterContactWindow(RegisterContactDesign):
    def __init__(self, user):
        self.user = user
        self.controller = ContactController(user)
        super().__init__()
        
    def add_contact(self):
        try:
            name = self.name.get()
            last_name = self.last_name.get()
            phone_num = int(self.phone_num.get())
            email = self.email.get()
            address = self.address.get()
            _type = self.cbx_type.get()
            emergency = self.emergency.get()

            if not self.are_valid_fields(name, phone_num, _type):
                messagebox.showwarning(message='Ingrese todos los datos', title='Advertencia')
                return

            contact = Contact(name, last_name, phone_num, _type, email, address, emergency)
            self.controller.insert_contact(contact)
            messagebox.showinfo(message='Contacto registrado correctamente')
            self.return_to_home()
        except ValueError:
            messagebox.showerror(message='Ingrese un número de teléfono válido')
        
    def return_to_home(self):
        from views.home import HomeWindow
        self.window.destroy()
        HomeWindow(self.user)
        
    def are_valid_fields(self, name, phone_num, _type):
        return name != '' and phone_num != None and _type != 'Seleccione una opción'
    
   