from rest_framework import serializers
from modules.authentication.handlers.user import UserHandler
from modules.authentication.models.user import User
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    user_handler = UserHandler()

    def validate(self, attrs):
        if attrs.get('email') is None:
            raise serializers.ValidationError("Email is required")
        if attrs.get('password') is None:
            raise serializers.ValidationError("Password is required")
        return attrs

    def login_user(self, validated_data: dict) -> dict:
        user = self.user_handler.get_user_by_email(validated_data.get('email'))
        if user is None:
            raise serializers.ValidationError("User not found")

        # if not user.check_password(validated_data['password']):
        #     raise serializers.ValidationError("Invalid password")

        refresh = RefreshToken.for_user(user)
        return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
