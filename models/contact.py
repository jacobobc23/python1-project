class Contact:
    def __init__(self, name, last_name, phone_number, type_contact, email = None, address = None, emergency = False, blocked = False, id = None):
        self.__name = name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__type_contact = type_contact
        self.__email = email
        self.__address = address
        self.__emergency = emergency
        self.__blocked = blocked
        self.__id = id
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name
        
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, new_number):
        self.__phone_number = new_number    
        
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, new_address):
        self.__address = new_address
    
    @property
    def emergency(self):
        return self.__emergency
    
    @emergency.setter
    def emergency(self, new_emergency):
        self.__emergency = new_emergency
    
    @property
    def type_contact(self):
        return self.__type_contact
    
    @type_contact.setter
    def type_contact(self, new_type):
        self.__type_contact = new_type
    
    @property
    def blocked(self):
        return self.__blocked
    
    @blocked.setter
    def blocked(self, new_status):
        self.__blocked = new_status
    
    @property
    def id(self):
        return self.__id
    
    def __str__(self):
        return f'ID: {self.__id}\nNombre: {self.__name} {self.__last_name}\nTeléfono: {self.__phone_number}\nCorreo: {self.__email}\nDirección: {self.__address}\nDe emergencia: {self.__emergency}\nTipo: {self.__type_contact}\nBloqueado: {self.__blocked}'
