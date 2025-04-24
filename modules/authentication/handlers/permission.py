from modules.authentication.repositorys.permission import PermissionRepository


class PermissionHandler:
    def __init__(self, permission_service=None):
        self.permission_service = permission_service if permission_service else PermissionRepository()
    
    def create_permission(self, permission_data: dict) -> dict:
        return self.permission_service.create_permission(permission_data)
    
    def get_permission_by_id(self, permission_id: int) -> dict:
        return self.permission_service.get_permission_by_id(permission_id)
    
    def update_permission(self, permission_id: int, permission_data: dict) -> dict:
        return self.permission_service.update_permission(permission_id, permission_data)
    
    def delete_permission(self, permission_id: int) -> bool:
        return self.permission_service.delete_permission(permission_id)
    
    def get_permission_by_name(self, name: str) -> dict:
        return self.permission_service.get_permission_by_name(name)
    
    def get_all_permissions(self) -> list:
        return self.permission_service.get_all_permissions()
    