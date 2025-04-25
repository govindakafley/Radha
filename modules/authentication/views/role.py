from modules.authentication.serializers.role import RoleSerializer
from modules.authentication.handlers.role import RoleHandler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

class RoleView(APIView):
    serializer_class = RoleSerializer
    # authentication_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Role created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        try:
            role_id = kwargs.get('id')
            if role_id:
                role = self.serializer_class.get_role_by_id(role_id)
                if role:
                    serialized = self.serializer_class(role).data
                    return Response(serialized, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = self.serializer_class()
                roles = serializer.get_all_roles()
                serialized = self.serializer_class(roles, many=True).data
                return Response(serialized, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        try:
            role_id = kwargs.get('id')
            if not role_id:
                return Response({"message": "Role ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            role = self.serializer_class.get_role_by_id(role_id)
            if not role:
                return Response({"message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(instance=role, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Role updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            role_id = kwargs.get('id')
            if not role_id:
                return Response({"message": "Role ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            role = self.serializer_class.get_role_by_id(role_id)
            if not role:
                return Response({"message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(instance=role)
            serializer.delete(role)
            return Response({"message": "Role deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_role_by_name(self, request, *args, **kwargs):
        try:
            name = kwargs.get('name')
            if not name:
                return Response({"message": "Role name is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            role = self.serializer_class.get_role_by_name(name)
            if not role:
                return Response({"message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serialized = self.serializer_class(role).data
            return Response(serialized, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)            
