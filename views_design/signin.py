import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class SigninDesign:
    def __init__(self):
        self.init_window()
        
    def init_window(self):
        self.window = tk.Tk()
        self.window.title('Iniciar sesión')
        self.window.geometry('1000x400')
        self.window.config(bg='white')
        self.window.resizable(False, False)
        self.init_components()
        self.window.mainloop()
    
    def init_components(self):
        
        left_panel = tk.Frame(self.window, width=500, bg='white')
        left_panel.pack(side='left', expand=tk.YES, fill=tk.BOTH)
        
        lbl_title = tk.Label(left_panel, text='Iniciar sesión', font=('Segoe UI', 25, BOLD), bg='white', pady=30)
        lbl_title.pack(expand=tk.YES, fill=tk.BOTH)
        
        form_panel = tk.Frame(left_panel, height=50, bg='white', padx=100)
        form_panel.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        
        lbl_email = tk.Label(form_panel, text='Correo', font=('Arial', 14), bg='white', anchor='w')
        lbl_email.pack(fill=tk.X, padx=20, pady=5)
        
        self.email = ttk.Entry(form_panel, font=('Arial', 10))
        self.email.pack(fill=tk.X, padx=20, pady=10)
        
        lbl_password = tk.Label(form_panel, text='Contraseña', font=('Arial', 14), bg='white', anchor='w')
        lbl_password.pack(fill=tk.X, padx=20, pady=5)
        
        self.password = ttk.Entry(form_panel, font=('Arial', 10))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show='*')    
        
        btn_signin = tk.Button(form_panel, text='INGRESAR', font=('Segoe UI', 14, BOLD), bg='black', bd=0, fg='white', cursor='hand2', command=self.signin)
        btn_signin.pack(fill=tk.X, padx=20, pady=20)
        
        right_panel = tk.Frame(self.window, bd=0, width=500, relief=tk.SOLID, bg='black')
        right_panel.pack(side='right', fill=tk.BOTH, expand=True)
        
        panel_signup = tk.Frame(right_panel, height=50, bd=0, relief=tk.SOLID)
        panel_signup.pack(side='top', fill=tk.X)
        
        lbl_signup = tk.Label(panel_signup, text='Crea tu cuenta!', font=('Segoe UI', 25, BOLD), bg='black', fg='white', pady=30)
        lbl_signup.pack(expand=tk.YES, fill=tk.BOTH)
        
        lbl_signup_info = tk.Label(right_panel, text='Registrate con tus datos y empieza con nosotros', font=('Segoe UI', 12), bg='black', fg='white', pady=10)
        lbl_signup_info.pack(fill=tk.X, padx=20)
        
        btn_signup = tk.Button(right_panel, text='REGISTRARSE', font=('Segoe UI', 14, BOLD), bg='white', fg='black', bd=0, cursor='hand2', command=self.signup)
        btn_signup.pack(padx=20, pady=20)
        
    




