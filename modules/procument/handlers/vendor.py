from modules.procument.resposiory.vendor import VendorRepository


class VendorHandler:
    def __init__(self):
        self.vendor_service = VendorRepository()

    def create_vendor(self, vendor_data: dict) -> dict:
        return self.vendor_service.create_vendor(vendor_data)

    def get_vendor_by_id(self, vendor_id: str) -> dict:
        return self.vendor_service.get_vendor_by_id(vendor_id)

    def update_vendor(self, vendor_id: str, vendor_data: dict) -> dict:
        return self.vendor_service.update_vendor(vendor_id, vendor_data)

    def delete_vendor(self, vendor_id: str) -> bool:
        return self.vendor_service.delete_vendor(vendor_id)

    def get_vendor_by_name(self, vendor_name: str) -> dict:
        return self.vendor_service.get_vendor_by_name(vendor_name)
    
    def get_vendor_by_mobile(self, mobile: str) -> dict:
        return self.vendor_service.get_vendor_by_mobile(mobile)
    

    def get_all_vendors(self) -> list:
        return self.vendor_service.get_all_vendors()    