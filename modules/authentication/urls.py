from django.urls import path
from modules.authentication.views.permission import PermissionView
from modules.authentication.views.user import RegisterView
from modules.authentication.views.login import LoginView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('register/<int:id>', RegisterView.as_view(), name='register_with_id'),
    path('permission', PermissionView.as_view(), name='permissions'),
    path('login', LoginView.as_view(), name='login'),
]
