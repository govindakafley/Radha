from django.db import models
import uuid
class Vendor(models.Model):
    vendor_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    vendor_name = models.CharField(max_length=100)
    vendor_phone = models.CharField(max_length=15, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'procument"."vendor'
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendor'

    def __str__(self):
        return self.vendor_name
