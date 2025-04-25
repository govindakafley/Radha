from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from modules.master.handlers.accountgroup import AccountGroupHandler
from modules.master.models.accountgroup import AccountGroup
from django.db.models import Max

class AccountGroupSerializer(serializers.ModelSerializer):
    account_group = AccountGroupHandler()
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','code', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    def validate(self, attrs):
        name = attrs.get('name') 
        if self.instance is None and self.account_group.get_account_group_by_name(name=name) is not None:
            raise serializers.ValidationError(_("Account group with this name already exists"))
        return attrs
    
    def create(self, validated_data):
        code = self.account_group.get_all_account_groups()
        if code:
            max_code = code.aggregate(max_code=Max('code'))['max_code']
            code = int(max_code) + 1
        else:
            code = 1

        f_code = str(code).zfill(4)

        data = {
            'name': validated_data['name'],
            'code': f_code,
        }  
        
        account_group = self.account_group.create_account_group(data)
        return account_group

    def update(self, instance, validated_data):
       account_group = self.account_group.update_account_group(instance.id, validated_data)
       return account_group
    
    def delete(self, instance):
        account_group = self.account_group.delete_account_group(instance.id)
        return account_group
    
    def get_account_group_by_name(self, name):
        account_group = self.account_group.get_account_group_by_name(name)
        return account_group
    
    def get_account_group_by_id(self, account_group_id):
        account_group = self.account_group.get_account_group_by_id(account_group_id)
        return account_group
    
    def get_all_account_groups(self):
        account_groups = self.account_group.get_all_account_groups()
        return account_groups
    
    def get_account_group_by_code(self, code):
        account_group = self.account_group.get_account_group_by_code(code)
        return account_group