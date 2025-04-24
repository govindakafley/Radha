from modules.authentication.repositorys.user import UserRepository


class UserHandler:
    def __init__(self, user_service=None):
        self.user_service = user_service
        self.repository = UserRepository()
        self.user_service = user_service if user_service else UserRepository()

    def create_user(self, user_data: dict) -> dict:
        return self.user_service.create_user(user_data)   

    def get_user_by_id(self, user_id: int)-> dict:
        return self.user_service.get_user_by_id(user_id)
    
    def update_user(self, user_id: int, user_data: dict) -> dict:
        return self.user_service.update_user(user_id, user_data)
    
    def delete_user(self, user_id: int):
        return self.user_service.delete_user(user_id)
    
    def get_all_users(self)-> list:
        return self.user_service.get_all_users()
    
    def get_user_by_email(self, email:str)-> dict:
        user =  self.user_service.get_user_by_email(email) 
        print('user', user)
        return user