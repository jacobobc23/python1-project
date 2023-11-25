from tkinter import messagebox
from controllers.login_controller import LoginController  
from exceptions.user_exceptions import CredentialsException
from views_design.signin import SigninDesign


class SigninWindow(SigninDesign):
    def __init__(self):
        self.controller = LoginController()
        super().__init__()

    def signin(self):
        from views.home import HomeWindow

        email = self.email.get()
        password = self.password.get()

        if not self.are_valid_fields(email, password):
            messagebox.showwarning(message='Ingrese los datos', title='Advertencia')
            return

        try: 
            user = self.controller.auth_user(email, password)
            self.window.destroy()
            HomeWindow(user)
        except CredentialsException as ex:
            messagebox.showerror(message=ex, title='Advertencia')
    
    def signup(self):
        from views.signup import SignupWindow
        self.window.destroy()
        SignupWindow()
    
    def are_valid_fields(self, email, password):
        return email != '' and password != ''
    
    