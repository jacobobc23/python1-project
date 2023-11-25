class User:
    def __init__(self, name, email, password, id = None):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password
        
    @property
    def id(self):
        return self.__id 
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, new_password):
        self.__password = new_password
    
    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.name}, Correo: {self.email}, Contraseña: {self.password}'
    
    