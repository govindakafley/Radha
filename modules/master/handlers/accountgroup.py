from modules.master.repository.accountgroup import AccountGroupRepository

class AccountGroupHandler:
    def __init__(self):
        self.account_group = AccountGroupRepository()

    def create_account_group(self, account_group_data: dict) -> dict:
        return self.account_group.create_account_group(account_group_data)
    
    def get_account_group_by_id(self, account_group_id: int) -> dict:

        return self.account_group.get_account_group_by_id(account_group_id)
    

    def update_account_group(self, account_group_id: int, account_group_data: dict) -> dict:

        return self.account_group.update_account_group(account_group_id, account_group_data)
    
    def delete_account_group(self, account_group_id: int) -> bool:
        return self.account_group.delete_account_group(account_group_id)
    
    def get_account_group_by_name(self, name: str) -> dict:
        return self.account_group.get_account_group_by_name(name)
    
    def get_all_account_groups(self) -> list:
        return self.account_group.get_all_account_groups()
    
    def get_account_group_by_code(self, code: str) -> dict:
        return self.account_group.get_account_group_by_code(code)
    
