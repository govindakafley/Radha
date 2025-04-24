from rest_framework import serializers
from modules.authentication.handlers.user import UserHandler
from modules.authentication.models.user import User

class RegisterUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}
    
    user_handler = UserHandler()

    def validate(self,attrs):
        if self.instance is None and self.user_handler.get_user_by_email(attrs['email']):
            raise serializers.ValidationError("Email already exists")

        return attrs

    def create(self, validate_data: dict)-> dict:
        user = self.user_handler.create_user(validate_data)
        user.save()
        return user
    
    def update(self, instance: dict, validated_data: dict):
        print(validated_data)
        user = self.user_handler.update_user(instance.id, validated_data) 
        return user
    
    def delete(self, instance: dict)->bool:
        user = self.user_handler.delete_user(instance.id) 
        user.save()
        return user
    
    def get_user_by_email(self, email: str)-> dict:
        user = self.user_handler.get_user_by_email(email) 
        return user
    
    def get_user_by_id(self, user_id: int)-> dict:
        user = self.user_handler.get_user_by_id(user_id) 
        return user
    
    def get_all_users(self)-> list:
        users = self.user_handler.get_all_users() 
        return users  