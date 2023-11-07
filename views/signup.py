from tkinter import messagebox
from controllers.user_controller import UserController
from exceptions.user_exceptions import UserAlreadyRegisteredException
from models.user import User
from views.signin import SigninWindow
from views_design.signup import SignupDesign


class SignupWindow(SignupDesign):
    def __init__(self):
        self.controller = UserController()
        super().__init__()    
        
    def create_account(self):
        
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        
        if not self.are_valid_fields(name, email, password):
            messagebox.showwarning(message='Ingrese todos los datos', title='Advertencia')
            return

        try:
            user = User(name, email, password)
            self.controller.insert_user(user)
            
            messagebox.showinfo(message='Registro existoso, bienvenido')
            self.return_to_login()
        except UserAlreadyRegisteredException as ex:
            messagebox.showerror(message=ex)

    def return_to_login(self):
        self.window.destroy()
        SigninWindow()

    def are_valid_fields(self, name, email, password):
       return name != '' and email != '' and password != ''