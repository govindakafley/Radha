
from django.utils.translation import gettext_lazy as _
from modules.authentication.models.permission import Permission

class PermissionRepository:
    @staticmethod
    def create_permission(permission_data: dict) -> dict:
        permission: Permission = Permission.objects.create(**permission_data)
        return permission
    
    @staticmethod
    def get_permission_by_id(permission_id: int) -> dict:
        try:
            permission: Permission = Permission.objects.get(id=permission_id)
            return permission
        except Permission.DoesNotExist:
            return None

    @staticmethod
    def update_permission(permission_id: int, permission_data: dict)->dict:
        try:
            permission: Permission = PermissionRepository.get_permission_by_id(permission_id)
            for attr, value in permission_data.items():
                setattr(permission, attr, value)
            permission.save()
            return permission
        except Permission.DoesNotExist:
            return None
       
    @staticmethod
    def delete_permission(permission_id: int) -> bool:
        try:
            permission: Permission = Permission.objects.get(id=permission_id)
            permission.delete()
            return True
        except Permission.DoesNotExist:
            return False
    @staticmethod
    def get_permission_by_name(name: str) -> dict:
        print('name', name)
        try:
            permission = Permission.objects.filter(name=name).first()
            print('dddddds',permission)
            return permission
        except Permission.DoesNotExist:
            return None
        
    @staticmethod
    def get_all_permissions() -> list:
        return Permission.objects.all()    