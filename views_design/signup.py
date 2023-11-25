import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class SignupDesign:
    def __init__(self):
        self.init_window()
    
    def init_window(self):
        self.window = tk.Tk()
        self.window.title('Crear cuenta')
        self.window.geometry('1000x500')
        self.window.config(bg='white')
        self.window.resizable(False, False)
        self.init_components()
        self.window.mainloop()
    
    def init_components(self):
        left_panel = tk.Frame(self.window, width=500, bg='black')
        left_panel.pack(side='left', fill=tk.BOTH, expand=True)

        panel_welcome = tk.Frame(left_panel, height=50)
        panel_welcome.pack(side='top')
        
        lbl_welcome = tk.Label(panel_welcome, text='Bienvenido de nuevo!', font=('Segoe UI', 25, BOLD), bg='black', fg='white', pady=30)
        lbl_welcome.pack(fill=tk.BOTH)
        
        lbl_signin_info = tk.Label(left_panel, text='Si ya tienes tu cuenta, ingresa con tus datos', font=('Segoe UI', 12), bg='black', fg='white')
        lbl_signin_info.pack(fill=tk.X)
        
        btn_signin = tk.Button(left_panel, text='INICIAR SESIÓN', font=('Segoe UI', 14, BOLD), bg='white', fg='black', bd=0, cursor='hand2', command=self.return_to_login)
        btn_signin.pack(padx=20, pady=20)
        
        right_panel = tk.Frame(self.window, bd=0, width=500, bg='white')
        right_panel.pack(side='right', expand=True, fill=tk.BOTH)
        
        title_panel = tk.Frame(right_panel, height=50)
        title_panel.pack(side='top', fill=tk.X)
        
        lbl_title = tk.Label(title_panel, text='Crear Cuenta', font=('Segoe UI', 25, BOLD), bg='white', pady=30)
        lbl_title.pack(fill=tk.BOTH)
        
        form_panel = tk.Frame(right_panel, height=50, bg='white', padx=100)
        form_panel.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        
        lbl_name = tk.Label(form_panel, text='Nombre', font=('Arial', 14), bg='white', anchor='w')
        lbl_name.pack(fill=tk.X, padx=20, pady=5)
        
        self.name = ttk.Entry(form_panel, font=('Arial', 10))
        self.name.pack(fill=tk.X, padx=20, pady=10)
        
        lbl_email = tk.Label(form_panel, text='Correo', font=('Arial', 14), bg='white', anchor='w')
        lbl_email.pack(fill=tk.X, padx=20, pady=5)
        
        self.email = ttk.Entry(form_panel, font=('Arial', 10))
        self.email.pack(fill=tk.X, padx=20, pady=10)
        
        lbl_password = tk.Label(form_panel, text='Contraseña', font=('Arial', 14), bg='white', anchor='w')
        lbl_password.pack(fill=tk.X, padx=20, pady=5)
        
        self.password = ttk.Entry(form_panel, font=('Arial', 10))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        
        btn_signup = tk.Button(form_panel, text='REGISTRARSE', font=('Segoe UI', 14, BOLD), bg='black', fg='white', cursor='hand2', command=self.create_account)
        btn_signup.pack(padx=20, pady=20)
        
        
   
    