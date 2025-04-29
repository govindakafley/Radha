
from django.urls import path

from modules.employee.views.employee import EmployeeView

urlpatterns = [
    path('employee',EmployeeView.as_view(), name='employee'),
]
