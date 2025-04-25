from django.apps import AppConfig


class MasterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.master'

    def ready(self):
        from .models.accountgroup import AccountGroup
