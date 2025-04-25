from modules.authentication.repositorys.role import RoleRepository


class RoleHandler:
    def __init__(self, role_repository =None):
        self.role_repository = RoleRepository()

    def create_role(self, role_data: dict) -> dict:
        return self.role_repository.create_role(role_data)

    def get_role_by_id(self, role_id: int) -> dict:
        return self.role_repository.get_role_by_id(role_id)

    def update_role(self, role_id: int, role_data: dict) -> dict:
        return self.role_repository.update_role(role_id, role_data)

    def delete_role(self, role_id: int) -> bool:
        return self.role_repository.delete_role(role_id)

    def get_role_by_name(self, name: str) -> dict:
        return self.role_repository.get_role_by_name(name)

    def get_all_roles(self) -> list:
        return self.role_repository.get_all_roles()