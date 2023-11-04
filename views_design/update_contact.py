import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class UpdateContactDesign:
    def __init__(self, contact):
        self.contact = contact
        self.init_window()
        
    def init_window(self):
        self.window = tk.Tk()
        self.window.title(f'Editar contacto: {self.contact.name}')
        self.window.geometry('850x500')
        self.window.config(bg='#FFFFFF')
        self.window.resizable(False, False)
        self.init_components()
        self.show_contact_data()
        self.window.mainloop()

    def init_components(self):
        bg_panel = tk.Frame(self.window, bd=0, width=800, relief=tk.SOLID, bg='white')
        bg_panel.pack(expand=tk.YES, fill=tk.X)
        
        title_panel = tk.Frame(bg_panel, height=50, bd=0, relief=tk.SOLID)
        title_panel.pack(side='top',fill=tk.X)
        
        lbl_title = tk.Label(title_panel, text='Editar contacto', font=('Segoe UI', 18, BOLD), bg='white', pady=30)
        lbl_title.pack(expand=tk.YES, fill=tk.BOTH)
        
        form_panel = tk.Frame(bg_panel, height=50, bd=0, relief=tk.SOLID, bg='white', padx=100)
        form_panel.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        
        lbl_name = tk.Label(form_panel, text='Nombre *', font=('Arial', 12), bg='white', anchor='w', padx=20)
        lbl_name.grid(row=0, column=0, sticky='w')
        
        self.name = ttk.Entry(form_panel, font=('Arial', 10), width=40)
        self.name.grid(row=1, column=0, pady=10, sticky='w', padx=20)
        
        lbl_last_name = tk.Label(form_panel, text='Apellido (opcional)', font=('Arial', 12), bg='white', anchor='w', padx=20)
        lbl_last_name.grid(row=0, column=1, sticky='w')
        
        self.last_name = ttk.Entry(form_panel, font=('Arial', 10), width=40)
        self.last_name.grid(row=1, column=1, pady=10, sticky='w', padx=20)
        
        lbl_phone = tk.Label(form_panel, text='Teléfono *', font=('Arial', 12), bg='white', anchor='w', padx=20)
        lbl_phone.grid(row=2, column=0, sticky='w')
            
        self.phone_num = ttk.Entry(form_panel, font=('Arial', 10), width=40)
        self.phone_num.grid(row=3, column=0, pady=10, sticky='w', padx=20)
        
        lbl_email = tk.Label(form_panel, text='Correo (opcional)', font=('Arial', 12), bg='white', anchor='w', padx=20)
        lbl_email.grid(row=2, column=1, sticky='w')
        
        self.email = ttk.Entry(form_panel, font=('Arial', 10), width=40)
        self.email.grid(row=3, column=1, pady=10, sticky='w', padx=20)
        
        lbl_address = tk.Label(form_panel, text='Dirección (opcional)', font=('Arial', 12), bg='white', anchor='w', padx=20)
        lbl_address.grid(row=4, column=0, sticky='w')
        
        self.address = ttk.Entry(form_panel, font=('Arial', 10), width=40)
        self.address.grid(row=5, column=0, pady=10, sticky='w', padx=20)
        
        lbl_type = tk.Label(form_panel, text='Tipo *', font=('Arial', 12), bg='white', anchor='w', padx=20)
        lbl_type.grid(row=4, column=1, sticky='w')
        
        self.cbx_type = ttk.Combobox(form_panel, state='readonly', width=43)
        self.cbx_type['values'] = ('Seleccione una opción', 'General', 'Familiar', 'Amigo', 'Trabajo')
        self.cbx_type.set('Seleccione una opción')
        self.cbx_type.grid(row=5, column=1, sticky='w', padx=20)
        
        self.emergency = tk.BooleanVar()
        self.chbx_emergency = tk.Checkbutton(form_panel, text='Contacto de emergencia', bg='white', width=40, variable=self.emergency)
        self.chbx_emergency.grid(row=6, column=0, sticky='w')
        
        btn_cancel = tk.Button(form_panel, text='CANCELAR', font=('Segoe UI', 10, BOLD), bg='red', fg='white',padx=30, bd=0, cursor='hand2', command=self.return_to_home)
        btn_cancel.grid(row=7, column=0, padx=20, pady=20)
        
        btn_add = tk.Button(form_panel, text='ACTUALIZAR', font=('Segoe UI', 10, BOLD), bg='blue', fg='white', padx=30, bd=0, cursor='hand2', command=self.update_contact)
        btn_add.grid(row=7, column=1, padx=20, pady=20)        
    
    def show_contact_data(self):
        self.name.insert(0, self.contact.name)
        self.phone_num.insert(0, self.contact.phone_number)
        
        if self.contact.last_name is not None:
            self.last_name.insert(0, self.contact.last_name)
        
        if self.contact.email is not None:
            self.email.insert(0, self.contact.email)
            
        if self.contact.address is not None:
            self.address.insert(0, self.contact.address)
            
        combo_values = ('General', 'Familiar', 'Amigo', 'Trabajo')
        if self.contact.type_contact in combo_values:
            self.cbx_type.set(self.contact.type_contact)
        
        if self.contact.emergency:
            self.chbx_emergency.select()
        else:
            self.chbx_emergency.deselect()
        
        