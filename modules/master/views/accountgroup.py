from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from modules.master.serializers.accountgroup import AccountGroupSerializer

class AccountGroupView(APIView):
    
    serializer_class = AccountGroupSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Account group created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            account_group_id = kwargs.get('id')
            if account_group_id:
                account_group = self.serializer_class.get_account_group_by_id(account_group_id)
                if account_group:
                    serialized = self.serializer_class(account_group).data
                    return Response(serialized, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Account group not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = self.serializer_class()
                account_groups = serializer.get_all_account_groups()
                serialized = self.serializer_class(account_groups, many=True).data
                return Response(serialized, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            account_group_id = kwargs.get('id')
            if not account_group_id:
                return Response({"message": "Account group ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            account_group = self.serializer_class.get_account_group_by_id(account_group_id)
            if not account_group:
                return Response({"message": "Account group not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(instance=account_group, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Account group updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            account_group_id = kwargs.get('id')
            if not account_group_id:
                return Response({"message": "Account group ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            account_group = self.serializer_class.get_account_group_by_id(account_group_id)
            if not account_group:
                return Response({"message": "Account group not found"}, status=status.HTTP_404_NOT_FOUND)
            
            account_group.delete()
            return Response({"message": "Account group deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_account_group_by_name(self, request, *args, **kwargs):
        try:
            name = kwargs.get('name')
            if not name:
                return Response({"message": "Account group name is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            account_group = self.serializer_class.get_account_group_by_name(name)
            if not account_group:
                return Response({"message": "Account group not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serialized = self.serializer_class(account_group).data
            return Response(serialized, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)  

                     