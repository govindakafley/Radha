from modules.procument.views.purchase_order import PurchaseOrderView
from modules.procument.views.vendor import VendorView
from django.urls import path

urlpatterns = [
    path('vendors', VendorView.as_view(), name='vendor'),
    path('purchase_orders', PurchaseOrderView.as_view(), name='purchase_order'),
]
