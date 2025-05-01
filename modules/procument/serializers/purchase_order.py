from rest_framework import serializers

from modules.procument.handlers.purchase_order import PurchaseOrderHandler
from modules.procument.models.purchase_order import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor_id = serializers.CharField(source='vendor.vendor_id', read_only=True)
    purchase_order_handler = PurchaseOrderHandler()
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'supplier': {'required': True},
            'order_date': {'required': True},
            'status': {'required': True},
        }
    def validators(self, attrs):
        order_number = attrs.get('order_number')
        order_name = attrs.get('order_name')
        order_description = attrs.get('order_description')
        order_quantity = attrs.get('order_quantity')
        order_unit = attrs.get('order_unit')
        order_price = attrs.get('order_price')
        status = attrs.get('status')

        if not order_number or not order_name or not order_description or not order_quantity or not order_unit or not order_price or not status:
            raise serializers.ValidationError("All fields are required.")
        if order_quantity <= 0:
            raise serializers.ValidationError("Order quantity must be greater than 0.")
        if order_price <= 0:
            raise serializers.ValidationError("Order price must be greater than 0.")
        
        if status not in ['Pending', 'Completed']:
            raise serializers.ValidationError("Status must be either 'Pending' or 'Completed'.")
        return attrs
    
    def create(self, validated_data):
        purchase_order = self.purchase_order_handler.create_purchase_order(validated_data)
        return purchase_order    
    
    def update(self, instance, validated_data):
        purchase_order = self.purchase_order_handler.update_purchase_order(instance.purchase_order_id, validated_data)
        return purchase_order
    
    def delete(self, instance):
        purchase_order = self.purchase_order_handler.delete_purchase_order(instance.purchase_order_id)
        return purchase_order
    
    def get(self, instance):
        purchase_order = self.purchase_order_handler.get_purchase_order(instance.purchase_order_id)
        return purchase_order
    
    def get_all(self):
        purchase_orders = self.purchase_order_handler.get_all_purchase_orders()
        return purchase_orders
    
    