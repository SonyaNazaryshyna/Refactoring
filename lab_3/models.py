from datetime import datetime
from typing import List


class User:
    def __init__(self, user_id: int, name: str, email: str, password: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.orders: List[Order] = []  

    def register(self):
        print(f"{self.name} зареєстрований з email: {self.email}")

    def login(self, email: str, password: str) -> bool:
        return self.email == email and self.password == password

    def create_order(self):
        order = Order(order_id=len(self.orders)+1, user=self, date=datetime.now(), status="New")
        self.orders.append(order)
        return order

    def view_orders(self) -> List['Order']:
        return self.orders

class Product:
    def __init__(self, product_id: int, name: str, description: str, price: float, stock_quantity: int):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity: int):
        self.stock_quantity += quantity

    def get_price(self) -> float:
        return self.price

class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self) -> float:
        return self.product.price * self.quantity

class Order:
    def __init__(self, order_id: int, user: User, date: datetime, status: str):
        self.id = order_id
        self.user = user
        self.date = date
        self.status = status
        self.items: List[OrderItem] = []

    def add_product(self, product: Product, quantity: int):
        if quantity > product.stock_quantity:
            raise ValueError("Not enough stock")
        
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                product.stock_quantity -= quantity
                return
        
        self.items.append(OrderItem(product, quantity))
        product.stock_quantity -= quantity

    def remove_product(self, product: Product):
        self.items = [item for item in self.items if item.product.id != product.id]

    def calculate_total(self) -> float:
        return sum(item.get_subtotal() for item in self.items)

    def change_status(self, status: str):
        self.status = status
