from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from modules.procument.serializers.vendor import VendorSerializer

class VendorView(APIView):
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            vendor = serializer.save()
            return Response({
                "message": "Vendor created successfully", 
                "vendor": serializer.data
            }, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response({
                "message": "Validation error",
                "errors": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request, *args, **kwargs):
        try:
            vendor_id = kwargs.get('vendor_id')
            if vendor_id:
                vendor = self.serializer_class.get(vendor_id=vendor_id)
                if vendor:
                    return Response({
                        "message": "Vendor retrieved successfully",
                        "vendor": vendor
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "message": "Vendor not found"
                    }, status=status.HTTP_404_NOT_FOUND)
            else:
                vendor = self.serializer_class()
                vendors = vendor.get_all()
                data = self.serializer_class(vendors, many=True).data
                
                return Response({
                    "message": "Vendors retrieved successfully",
                    "vendors": data
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

    def put(self, request, *args, **kwargs):
        try:
            vendor_id = kwargs.get('vendor_id')
            if not vendor_id:
                return Response({
                    "message": "Vendor ID is required"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            vendor = self.serializer_class.get(vendor_id=vendor_id)
            if not vendor:
                return Response({
                    "message": "Vendor not found"
                }, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(instance=vendor, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            updated_vendor = serializer.save()
            return Response({
                "message": "Vendor updated successfully",
                "vendor": serializer.data
            }, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response({
                "message": "Validation error",
                "errors": ve.detail
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            vendor_id = kwargs.get('vendor_id')
            if not vendor_id:
                return Response({
                    "message": "Vendor ID is required"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            vendor = self.serializer_class.get(vendor_id=vendor_id)
            if not vendor:
                return Response({
                    "message": "Vendor not found"
                }, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.serializer_class(instance=vendor)
            serializer.delete()
            return Response({
                "message": "Vendor deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)         
