from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modules.authentication.serializers.register import RegisterUserSerializers
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    serializer_class = RegisterUserSerializers
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        self.authentication_classes = ['view_user']
        self.permission_classes = [IsAuthenticated] 
        try:
            user = self.serializer_class.Meta.model.objects.all()
            serializer = self.serializer_class(user, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        try:
            user = get_object_or_404(self.serializer_class.Meta.model, id=kwargs['id'])

            serializer = self.serializer_class(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
 
