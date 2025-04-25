
from modules.master.handlers.accountgroup import AccountGroupHandler
from modules.master.handlers.accounttypes import AccountTypesHandler
from modules.master.models.accounttypes import AccountTypes
from rest_framework import serializers

class AccountTypesSerializer(serializers.ModelSerializer):
    type_handler = AccountTypesHandler()
    group_handler = AccountGroupHandler()
    class Meta:
        model = AccountTypes
        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, attrs: dict) -> dict:
        if self.instance is None and self.type_handler.get_account_type_by_name(attrs.get('name')) is not None:
            raise serializers.ValidationError("Account type with this name already exists")
        
        if self.group_handler.get_account_group_by_code(attrs.get('code')) is None:
            raise serializers.ValidationError("Account type with this code is not exists")
        
        return attrs

    def create(self, validated_data: dict) -> dict:
        account_type = self.type_handler.create_account_type(validated_data)
        return account_type
    
    def update(self, instance: AccountTypes, validated_data: dict) -> dict:
        account_type = self.type_handler.update_account_type(instance.id, validated_data)
        return account_type
    
    def delete(self, instance: AccountTypes) -> bool:
        account_type = self.type_handler.delete_account_type(instance.id)
        return account_type
    
    def get_account_type_by_name(self, name: str) -> dict:
        account_type = self.type_handler.get_account_type_by_name(name)
        return account_type
    
    def get_account_type_by_id(self, account_type_id: int) -> dict:

        account_type = self.type_handler.get_account_type_by_id(account_type_id)
        return account_type
    
    def get_all_account_types(self) -> list:
        account_types = self.type_handler.get_all_account_types()
        return account_types
    