from modules.authentication.models.user import User

class UserRepository:
    @staticmethod
    def create_user(user_data:dict)-> dict:
        user: User = User.objects.create(**user_data)
        return user
    
    @staticmethod
    def get_user_by_id(user_id: int)->dict:
        try:
            user: User = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return None
    @staticmethod
    def get_user_by_email(email: str)->dict:
        try:
            user = User.objects.filter(email=email).first()
            return user
        except User.DoesNotExist:
            return None
        
    @staticmethod
    def update_user(user_id: int, user_data: dict)->dict:
        try:
            user:User = User.objects.get(id=user_id)
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()
            return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id: int)->bool:
        try:
            user: User = User.objects.get(id=user_id)
            user.delete()
            return True
        except User.DoesNotExist:
            return False

    @staticmethod
    def get_all_users()->list:
        return User.objects.all()
            