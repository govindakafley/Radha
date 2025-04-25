from modules.master.repository.accounttypes import AccountTypeRepository


class AccountTypesHandler:
    def __init__(self, account_types = None):
        self.account_types = AccountTypeRepository()

    def create_account_type(self, account_type_data: dict) -> dict:
        return self.account_types.create_account_type(account_type_data)
    
    def get_account_type_by_id(self, account_type_id: int) -> dict:
        return self.account_types.get_account_type_by_id(account_type_id)
    
    def update_account_type(self, account_type_id: int, account_type_data: dict) -> dict:
        return self.account_types.update_account_type(account_type_id, account_type_data)
    
    def delete_account_type(self, account_type_id: int) -> bool:
        return self.account_types.delete_account_type(account_type_id)
    
    def get_account_type_by_name(self, name: str) -> dict:
        return self.account_types.get_account_type_by_name(name)
    
    def get_all_account_types(self) -> list:
        return self.account_types.get_all_account_types()
    
    def get_account_type_by_code(self, code: str) -> dict:
        return self.account_types.get_account_type_by_code(code)
    