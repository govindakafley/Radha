from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from modules.master.serializers.accounttypes import AccountTypesSerializer
class AccountTypesView(APIView):
    serializer_class = AccountTypesSerializer  # Placeholder for the serializer class

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Account type created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        try:
            account_type_id = kwargs.get('id')
            if account_type_id:
                account_type = self.serializer_class.get_account_type_by_id(account_type_id)
                if account_type:
                    serialized = self.serializer_class(account_type).data
                    return Response(serialized, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Account type not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = self.serializer_class()
                account_types = serializer.get_all_account_types()
                serialized = self.serializer_class(account_types, many=True).data
                return Response(serialized, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)  

    def put(self, request, *args, **kwargs):
        try:
            account_type_id = kwargs.get('id')
            if not account_type_id:
                return Response({"message": "Account type ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            account_type = self.serializer_class.get_account_type_by_id(account_type_id)
            if not account_type:
                return Response({"message": "Account type not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(instance=account_type, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Account type updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            account_type_id = kwargs.get('id')
            if not account_type_id:
                return Response({"message": "Account type ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            account_type = self.serializer_class.get_account_type_by_id(account_type_id)
            if not account_type:
                return Response({"message": "Account type not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(instance=account_type)
            serializer.delete(account_type)
            return Response({"message": "Account type deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)    
