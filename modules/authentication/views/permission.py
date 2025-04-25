from modules.authentication.serializers.permission import PermissionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class PermissionView(APIView):
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Permission created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)    
    
    def get(self, request, *args, **kwargs):
        try:
            permission_id = kwargs.get('id')
            if permission_id:
                permission = self.serializer_class.get_permission_by_id(permission_id)
                if permission:
                    serialized = self.serializer_class(permission).data
                    return Response(serialized, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = self.serializer_class()
                permissions = serializer.get_all_permissions()
                serialized = self.serializer_class(permissions, many=True).data
                return Response(serialized, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
