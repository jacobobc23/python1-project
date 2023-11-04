from dao.user_dao import UserDao

class UserController:
    def __init__(self):
        self.user_dao = UserDao()
        
    def select_user(self, email):
        return self.user_dao.select_user(email)
    
    def insert_user(self, user):
        self.user_dao.insert_user(user)