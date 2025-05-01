from modules.procument.models.purchase_order import PurchaseOrder


class PurchaseOrderRepository:
    @staticmethod
    def create_purchase_order(purchase_order_data: dict) -> dict:
        try:
            purchase_order = PurchaseOrder.objects.create(**purchase_order_data)
            return purchase_order
        except Exception as e:
            return e
    @staticmethod
    def get_purchase_order_by_id(purchase_order_id: str) -> dict:
        try:
            purchase_order = PurchaseOrder.objects.get(purchase_order_id=purchase_order_id)
            return purchase_order
        except PurchaseOrder.DoesNotExist:
            return None
        except Exception as e:
            return e
    @staticmethod
    def update_purchase_order(purchase_order_id: str, purchase_order_data: dict) -> dict:
        try:
            purchase_order = PurchaseOrderRepository.get_purchase_order_by_id(purchase_order_id=purchase_order_id)
            for key, value in purchase_order_data.items():
                setattr(purchase_order, key, value)
            purchase_order.save()
            return purchase_order
        except PurchaseOrder.DoesNotExist:
            return None
        except Exception as e:
            return e

    @staticmethod
    def delete_purchase_order(purchase_order_id: str) -> bool:
        try:
            purchase_order = PurchaseOrderRepository.get_purchase_order_by_id(purchase_order_id=purchase_order_id)
            if purchase_order:
                purchase_order.delete()
                return True
            return False
        except Exception as e:
            return e

    @staticmethod
    def get_all_purchase_orders() -> list:
        try:
            purchase_orders = PurchaseOrder.objects.all()
            return purchase_orders
        except Exception as e:
            return e    
        
                