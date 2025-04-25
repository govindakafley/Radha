
from modules.master.models.accountgroup import AccountGroup

class AccountGroupRepository:

    @staticmethod
    def create_account_group(account_group_data: dict) -> dict:
        account_group: AccountGroup = AccountGroup.objects.create(**account_group_data)
        return account_group
    
    @staticmethod
    def get_account_group_by_id(account_group_id: int) -> dict:
        try:
            account_group: AccountGroup = AccountGroup.objects.get(id=account_group_id)
            return account_group
        except AccountGroup.DoesNotExist:
            return None

    @staticmethod
    def update_account_group(account_group_id: int, account_group_data: dict) -> dict:
        try:
            account_group: AccountGroup = AccountGroupRepository.get_account_group_by_id(account_group_id)
            for attr, value in account_group_data.items():
                setattr(account_group, attr, value)
            account_group.save()
            return account_group
        except AccountGroup.DoesNotExist:
            return None

    @staticmethod
    def delete_account_group(account_group_id: int) -> bool:
        try:
            account_group: AccountGroup = AccountGroup.objects.get(id=account_group_id)
            account_group.delete()
            return True
        except AccountGroup.DoesNotExist:
            return False

    @staticmethod
    def get_account_group_by_name(name: str) -> dict:
        try:
            account_group = AccountGroup.objects.filter(name=name).first()
            return account_group
        except AccountGroup.DoesNotExist:
            return None
    @staticmethod
    def get_account_group_by_code(code: str) -> dict:
        try:
            account_group = AccountGroup.objects.filter(code=code).first()
            return account_group
        except AccountGroup.DoesNotExist:
            return None
        
    @staticmethod
    def get_all_account_groups() -> list:
        return AccountGroup.objects.all()                