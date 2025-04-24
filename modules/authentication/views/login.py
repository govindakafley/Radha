from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from modules.authentication.serializers.login import LoginSerializer

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    # authentication_classes = []

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_data = serializer.login_user(serializer.validated_data)

            response = Response({'message': 'Login successfully'}, status=200)
            response.set_cookie(key='access_token', value=user_data['access_token'], httponly=True, secure=True, samesite='None')
            response.set_cookie(key='refresh_token', value=user_data['refresh_token'], httponly=True, secure=True, samesite='None')
            return response
        
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=400)
        
        except Exception as e:
            return Response({'error': f'An unexpected error occurred: {str(e)}'}, status=500)
