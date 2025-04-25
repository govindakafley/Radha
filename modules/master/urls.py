from django.urls import path
from modules.master.views.accountgroup import AccountGroupView


urlpatterns = [
    path('account_group',AccountGroupView.as_view(), name='account_group'),
]
