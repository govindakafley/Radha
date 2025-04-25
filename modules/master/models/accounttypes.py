from django.db import models

from modules.master.models.accountgroup import AccountGroup
class AccountTypes(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "account_types"
        verbose_name = "Account Types"
        verbose_name_plural = "Account Types"

    def __str__(self):
        return self.name
