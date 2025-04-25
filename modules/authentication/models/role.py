from django.db import models

from modules.authentication.models.permission import Permission
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(Permission, related_name='roles', blank=True)

    class Meta:
        db_table = 'authentication_role'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ['name']
        
    def __str__(self):
        return self.name