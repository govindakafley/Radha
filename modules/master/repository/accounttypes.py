
from modules.master.models.accounttypes import AccountTypes

class AccountTypeRepository:
    @staticmethod
    def create_account_type(account_type_data: dict) -> dict:
        account_type: AccountTypes = AccountTypes.objects.create(**account_type_data)
        return account_type
    
    @staticmethod
    def get_account_type_by_id(account_type_id: int) -> dict:
        try:
            account_type: AccountTypes = AccountTypes.objects.get(id=account_type_id)
            return account_type
        except AccountTypes.DoesNotExist:
            return None

    @staticmethod
    def update_account_type(account_type_id: int, account_type_data: dict) -> dict:
        try:
            account_type: AccountTypes = AccountTypeRepository.get_account_type_by_id(account_type_id)
            for attr, value in account_type_data.items():
                setattr(account_type, attr, value)
            account_type.save()
            return account_type
        except AccountTypes.DoesNotExist:
            return None  

    @staticmethod
    def delete_account_type(account_type_id: int) -> bool:
        try:
            account_type: AccountTypes = AccountTypes.objects.get(id=account_type_id)
            account_type.delete()
            return True
        except AccountTypes.DoesNotExist:
            return False

    @staticmethod
    def get_account_type_by_name(name: str) -> dict:
        try:
            account_type = AccountTypes.objects.filter(name=name).first()
            return account_type
        except AccountTypes.DoesNotExist:
            return None

    @staticmethod
    def get_account_type_by_code(code: str) -> dict:
        try:
            account_type = AccountTypes.objects.filter(account_code=code).first()
            return account_type
        except AccountTypes.DoesNotExist:
            return None

    @staticmethod
    def get_all_account_types() -> list:
        return AccountTypes.objects.all()                  