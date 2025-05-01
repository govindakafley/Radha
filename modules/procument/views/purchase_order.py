from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from modules.procument.serializers.vendor import VendorSerializer
class PurchaseOrderView(APIView):
    serializer_class = VendorSerializer()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            purchase_order = serializer.save()
            return Response({
                "message": "Purchase order created successfully",
                "purchase_order": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            purchase_order_id = kwargs.get('purchase_order_id')
            purchase_order = self.serializer_class.get(purchase_order_id)
            if not purchase_order:
                return Response({
                    "message": "Purchase order not found"
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(instance=purchase_order, data=request.data)
            serializer.is_valid(raise_exception=True)
            purchase_order = serializer.save()
            return Response({
                "message": "Purchase order updated successfully",
                "purchase_order": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)    
        
    def delete(self, request, *args, **kwargs):
        try:
            purchase_order_id = kwargs.get('purchase_order_id')
            purchase_order = self.serializer_class.get(purchase_order_id)
            if not purchase_order:
                return Response({
                    "message": "Purchase order not found"
                }, status=status.HTTP_404_NOT_FOUND)
            purchase_order.delete()
            return Response({
                "message": "Purchase order deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        try:
            purchase_order_id = kwargs.get('purchase_order_id')
            purchase_order = self.serializer_class.get(purchase_order_id)
            if not purchase_order:
                return Response({
                    "message": "Purchase order not found"
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(instance=purchase_order)
            return Response({
                "message": "Purchase order retrieved successfully",
                "purchase_order": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)   

    def get_all(self, request, *args, **kwargs):
        try:
            purchase_orders = self.serializer_class.get_all()
            serializer = self.serializer_class(instance=purchase_orders, many=True)
            return Response({
                "message": "Purchase orders retrieved successfully",
                "purchase_orders": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST) 
       
        