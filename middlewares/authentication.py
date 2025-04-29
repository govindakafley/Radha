from rest_framework_simplejwt.authentication import JWTAuthentication

class CookiesJWTAuthentication(JWTAuthentication):
    print("CookiesJWTAuthentication initialized")
    def authentication(self, request):
        jwt_token = request.COOKIES.get('access_token')
        if jwt_token is None:
            return None
        
        validated_token = self.get_validated_token(jwt_token)
        user = self.get_user(validated_token)
        return user, validated_token