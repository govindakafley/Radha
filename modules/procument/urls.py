from modules.procument.views.vendor import VendorView
from django.urls import path

urlpatterns = [
    path('vendors', VendorView.as_view(), name='vendor'),
]
