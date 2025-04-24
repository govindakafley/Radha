from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS
from django.db import models
from django.utils.translation import gettext_lazy as _
class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Permission Name"))
    codename = models.CharField(max_length=100, unique=True, verbose_name=_("Permission Codename"))

    class Meta:
        db_table = _('authentication_permission')
        verbose_name = _("Permission")
        verbose_name_plural = _("Permissions")
        ordering = ['name']

    def __str__(self):
        return self.name
    
    
