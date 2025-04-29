from modules.procument.handlers.vendor import VendorHandler
from modules.procument.models.vendor import Vendor
from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    vendor_handler = VendorHandler()
    class Meta:
        model = Vendor
        fields = '__all__'
        read_only_fields = ['vendor_id', 'registration_date']

    def validate(self, attrs):
        if self.vendor_handler.get_vendor_by_mobile(attrs.get('vendor_phone')) is not None:
            raise serializers.ValidationError("Vendor with this phone number already exists.")
        return super().validate(attrs)
    
    def create(self, validated_data):
        vendor = self.vendor_handler.create_vendor(validated_data)
        return vendor
    
    def update(self, instance, validated_data):
        vendor = self.vendor_handler.update_vendor(instance.vendor_id, validated_data)
        return vendor
    
    def delete(self, instance):
        vendor = self.vendor_handler.delete_vendor(instance.vendor_id)
        return vendor
    
    def get(self, instance):
        vendor = self.vendor_handler.get_vendor_by_id(instance.vendor_id)
        return vendor
    
    def get_all(self):
        vendors = self.vendor_handler.get_all_vendors()
        return vendors
    
