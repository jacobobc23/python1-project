class UserAlreadyRegisteredException(Exception):
    def __init__(self, message='Ya se encuentra registrado'):
        super().__init__(message)
        
class CredentialsException(Exception):
    def __init__(self, message='Correo o contraseña incorrecta'):
        super().__init__(message)