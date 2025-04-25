from django.db import models
from django.utils.translation import gettext_lazy as _
class AccountGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "account_group"
        verbose_name = "Account Group"
        verbose_name_plural = "Account Groups"

    def __str__(self):
        return self.name