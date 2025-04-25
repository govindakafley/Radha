
from rest_framework import serializers
from modules.authentication.handlers.permission import PermissionHandler
from modules.authentication.models.permission import Permission
class PermissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')

    permission_handler = PermissionHandler()

    def validate(self, attrs: dict)-> dict:
        print('attrs', attrs)
        if self.instance is None and self.permission_handler.get_permission_by_name(name=attrs['name']) is not None:
            raise serializers.ValidationError("Permission with this name already exists")
        return attrs
    
    def create(self, validated_data: dict) -> dict:
        permission = self.permission_handler.create_permission(validated_data)
        permission.save()
        return permission
    
    def update(self, instance: Permission, validated_data: dict) -> dict:
        permission = self.permission_handler.update_permission(instance.id, validated_data) 
        return permission
    
    def delete(self, instance: Permission) -> bool:
        permission = self.permission_handler.delete_permission(instance.id) 
        permission.save()
        return permission
    
    def get_permission_by_name(self, name: str) -> dict:
        permission = self.permission_handler.get_permission_by_name(name) 
        return permission
    
    def get_permission_by_id(self, permission_id: int) -> dict:
        permission = self.permission_handler.get_permission_by_id(permission_id) 
        return permission
    
    def get_all_permissions(self) -> list:
        permissions = self.permission_handler.get_all_permissions() 
        return permissions
