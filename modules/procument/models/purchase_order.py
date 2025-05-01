from django.db import models
from modules.procument.models.vendor import Vendor
import uuid
class PurchaseOrder(models.Model):
    purchase_order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_number = models.CharField(max_length=20)
    order_name = models.CharField(max_length=100)
    order_description = models.TextField()
    order_quantity = models.IntegerField()
    order_unit = models.CharField(max_length=20)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    
    class Meta:
        db_table = 'procument"."purchase_order'
        verbose_name = 'Purchase Order'
        verbose_name_plural = 'Purchase Orders'
    





