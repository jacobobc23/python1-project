import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

class HomeDesign:
    def __init__(self):
        self.init_window()

    def fill_table(self, contacts : []):
        # toma todos los hijos (elementos) de la tabla, los desempaqueta para eliminarlos uno x uno
        self.table.delete(*self.table.get_children()) 

        for contact in contacts:
            values = (contact.name, contact.last_name, contact.phone_number, contact.email, contact.address,
                      'Si' if contact.emergency else 'No', contact.type_contact, 'Bloqueado@' if contact.blocked else 'Desbloquead@')
            self.table.insert('', 'end', text=f'{contact.id}', values=values)

    def init_window(self):
        self.window = tk.Tk()
        self.window.title(f'Contactos - {self.user.name}')
        self.window.geometry('1200x500')
        self.window.config(bg='white')
        self.window.resizable(False, False)
        self.init_components()
        self.window.mainloop()

    def init_components(self):
        bg_panel = tk.Frame(self.window, bd=0, width=800, relief=tk.SOLID, bg='white')
        bg_panel.pack(expand=tk.YES, fill=tk.BOTH)

        title_panel = tk.Frame(bg_panel, height=50, bd=0, relief=tk.SOLID)
        title_panel.pack(side='top', fill=tk.X)

        lbl_title = tk.Label(title_panel, text='Mi agenda', font=('Segoe UI', 18, BOLD), bg='white', pady=30)
        lbl_title.pack(expand=tk.YES, fill=tk.BOTH)

        search_panel = tk.Frame(bg_panel, height=50, bd=0, relief=tk.SOLID, bg='white', padx=80)
        search_panel.pack(fill=tk.X)

        self.filter = ttk.Entry(search_panel, font=('Arial', 10), width=30)  # Reduje el ancho del Entry
        self.filter.pack(side='left', padx=20, pady=10)

        search_button = tk.Button(search_panel, text='BUSCAR', font=('Segoe UI', 10, BOLD), padx=30, bg='lightgrey', fg='black', bd=0, cursor='hand2', command=self.search_contacts_by_filter)
        search_button.pack(side='left', padx=10, pady=10)

        all_button = tk.Button(search_panel, text='VER TODOS', font=('Segoe UI', 10, BOLD), padx=30, bg='lightgrey', fg='black', bd=0, cursor='hand2', command=self.show_all_contacts)
        all_button.pack(side='left', padx=10, pady=10)
        
        return_to_login = tk.Button(search_panel, text='Cerrar sesión', font=('Segoe UI', 10, BOLD), padx=30, bg='white', fg='red', bd=0, cursor='hand2', command=self.return_to_login)
        return_to_login.pack(side='right', padx=10, pady=10)

        data_panel = tk.Frame(bg_panel, height=50, bd=0, relief=tk.SOLID, bg='white', padx=100)
        data_panel.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        self.table = ttk.Treeview(data_panel, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8'))

        self.table.column('#0', width=30, anchor='center')
        self.table.column('col1', width=120, anchor='center')
        self.table.column('col2', width=120, anchor='center')
        self.table.column('col3', width=120, anchor='center')
        self.table.column('col4', width=120, anchor='center')
        self.table.column('col5', width=120, anchor='center')
        self.table.column('col6', width=120, anchor='center')
        self.table.column('col7', width=120, anchor='center')
        self.table.column('col8', width=120, anchor='center')

        self.table.heading('#0', text='#', anchor='center')
        self.table.heading('col1', text='Nombre', anchor='center')
        self.table.heading('col2', text='Apellido', anchor='center')
        self.table.heading('col3', text='Teléfono', anchor='center')
        self.table.heading('col4', text='Correo', anchor='center')
        self.table.heading('col5', text='Dirección', anchor='center')
        self.table.heading('col6', text='Emergencia', anchor='center')
        self.table.heading('col7', text='Tipo', anchor='center')
        self.table.heading('col8', text='Estado', anchor='center')

        self.table.grid(row=0, column=0, columnspan=5)

        btn_add = tk.Button(data_panel, text='AGREGAR', font=('Segoe UI', 10, BOLD), bg='blue', padx=30,  fg='white', bd=0, cursor='hand2', command=self.add_contact)
        btn_update = tk.Button(data_panel, text='EDITAR', font=('Segoe UI', 10, BOLD), bg='#FFD700', padx=30,  fg='white', bd=0, cursor='hand2', command=self.update_contact)
        btn_delete = tk.Button(data_panel, text='ELIMINAR', font=('Segoe UI', 10, BOLD), bg='red', padx=30,  fg='white', bd=0, cursor='hand2', command=self.delete_contact)
        btn_block = tk.Button(data_panel, text='BLOQUEAR', font=('Segoe UI', 10, BOLD), bg='black', padx=30,  fg='white', bd=0, cursor='hand2', command=self.block_contact)
        btn_unblock = tk.Button(data_panel, text='DESBLOQUEAR', font=('Segoe UI', 10, BOLD), bg='#4CAF50', padx=30,  fg='white', bd=0, cursor='hand2', command=self.unblock_contact)

        btn_add.grid(row=1, column=0, pady=10)
        btn_update.grid(row=1, column=1)
        btn_delete.grid(row=1, column=2)
        btn_block.grid(row=1, column=3)
        btn_unblock.grid(row=1, column=4)

        contacts = self.controller.list_contacts(self.user.id)
        self.fill_table(contacts)

