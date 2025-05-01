from modules.procument.resposiory.purchase_order import PurchaseOrderRepository

    
class PurchaseOrderHandler:
    def __init__(self):
        self.purchase_order = PurchaseOrderRepository()
        self.total_amount = 0

    def create_purchase_order(self, purchase_order_data: dict) -> dict:
        purchase_order_data['total_amount'] = self.calculate_total_amount(purchase_order_data)
        return self.purchase_order.create_purchase_order(purchase_order_data)
    
    def calculate_total_amount(self, purchase_order_data: dict) -> float:
        quantity = purchase_order_data.get('order_quantity', 0)
        price = purchase_order_data.get('order_price', 0.0)
        self.total_amount = quantity * price
        return self.total_amount
         

    def update_purchase_order(self, purchase_order_id: str, purchase_order_data: dict) -> dict:
        return self.purchase_order.update_purchase_order(purchase_order_id=purchase_order_id, purchase_order_data=purchase_order_data)

    def delete_purchase_order(self, purchase_order_id: str) -> bool:
        return self.purchase_order.delete_purchase_order(purchase_order_id=purchase_order_id)

    def get_purchase_order(self, purchase_order_id: str) -> dict:
        # Logic to get a purchase order
        return self.purchase_order.get_purchase_order_by_id(purchase_order_id=purchase_order_id)
    
    def get_all_purchase_orders(self) -> list:
        # Logic to get all purchase orders
        return self.purchase_order.get_all_purchase_orders()