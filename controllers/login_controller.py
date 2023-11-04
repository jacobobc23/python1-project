from dao.login_dao import LoginDao

class LoginController:
    def __init__(self):
        self.login_dao = LoginDao()
        
    def select_user(self, email, password):
        return self.login_dao.select_user(email, password)
    
    