from modules.authentication.models.role import Role

class RoleRepository:
    @staticmethod
    def create_role(role_data: dict) -> dict:
        role: Role = Role.objects.create(**role_data)
        return role
    
    @staticmethod
    def get_role_by_id(role_id: int) -> dict:
        try:
            role: Role = Role.objects.get(id=role_id)
            return role
        except Role.DoesNotExist:
            return None

    @staticmethod
    def update_role(role_id: int, role_data: dict) -> dict:
        try:
            role: Role = RoleRepository.get_role_by_id(role_id)
            for attr, value in role_data.items():
                setattr(role, attr, value)
            role.save()
            return role
        except Role.DoesNotExist:
            return None

    @staticmethod
    def delete_role(role_id: int) -> bool:
        try:
            role: Role = Role.objects.get(id=role_id)
            role.delete()
            return True
        except Role.DoesNotExist:
            return False
    @staticmethod
    def get_role_by_name(name: str) -> dict:
        try:
            role = Role.objects.filter(name=name).first()
            return role
        except Role.DoesNotExist:
            return None

    @staticmethod
    def get_all_roles() -> list:
        return Role.objects.all()            