from rest_framework import serializers
from modules.authentication.models.role import Role
from modules.authentication.handlers.role import RoleHandler

class RoleSerializer(serializers.ModelSerializer):
    role_handler = RoleHandler()
    class Meta:
        model = Role
        fields = ['id', 'name','permissions']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False},
        }

    def validate(self, attrs):
        name = attrs.get('name') 
        if self.instance is None and self.role_handler.get_role_by_name(name=name) is not None:
            raise serializers.ValidationError("Role with this name already exists")
        return attrs
    
    def create(self, validated_data):
        permission = validated_data.pop('permissions', None)
        role = self.role_handler.create_role(validated_data)
        if permission:
            role.permissions.set(permission)
        role.save()

        return role
    
    def update(self, instance, validated_data):
        permission = validated_data.pop('permissions', None)
        role = self.role_handler.update_role(instance.id, validated_data) 
        if permission:
            role.permissions.set(permission)
        role.save()
        return role
    
    def delete(self, instance):
        role = self.role_handler.delete_role(instance.id) 
        role.save()
        return role
    
    def get_role_by_name(self, name):
        role = self.role_handler.get_role_by_name(name) 
        return role
    
    def get_role_by_id(self, role_id):
        role = self.role_handler.get_role_by_id(role_id) 
        return role
    
    def get_all_roles(self):
        roles = self.role_handler.get_all_roles() 
        return roles