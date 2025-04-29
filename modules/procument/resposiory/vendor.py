from modules.procument.models.vendor import Vendor
class VendorRepository:
    @staticmethod
    def create_vendor(vendor_data: dict) -> dict:
        try:
            vendor = Vendor.objects.create(**vendor_data)
            return vendor
        except Exception as e:
            return e

    @staticmethod
    def get_vendor_by_id(vendor_id: str) -> dict:
        try:
            vendor = Vendor.objects.get(vendor_id=vendor_id)
            return vendor
        except Vendor.DoesNotExist:
            return None
        except Exception as e:
            return e
    @staticmethod
    def update_vendor(vendor_id: str, vendor_data: dict) -> dict:
        try:
            vendor = VendorRepository.get_vendor_by_id(vendor_id=vendor_id)
            for key, value in vendor_data.items():
                setattr(vendor, key, value)
            vendor.save()
            return vendor
        except Vendor.DoesNotExist:
            return None
        except Exception as e:
            return e   

    @staticmethod
    def delete_vendor(vendor_id: str) -> bool:
        try:
            vendor = VendorRepository.get_vendor_by_id(vendor_id=vendor_id)
            if vendor:
                vendor.delete()
                return True
            return False
        except Exception as e:
            return e

    @staticmethod
    def get_vendor_by_name(vendor_name: str) -> dict:
        try:
            vendor = Vendor.objects.get(vendor_name=vendor_name)
            return vendor
        except Vendor.DoesNotExist:
            return None
        except Exception as e:
            return e
        
    @staticmethod
    def get_vendor_by_mobile(mobile: str) -> dict:
        try:
            vendor = Vendor.objects.filter(vendor_phone=mobile).first()
            return vendor
        except Vendor.DoesNotExist:
            return None
        except Exception as e:
            return e    
    @staticmethod
    def get_all_vendors() -> list:
        try:
            vendors = Vendor.objects.all()
            return vendors
        except Exception as e:
            return e             