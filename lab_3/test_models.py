import unittest
from datetime import datetime
from models import User, Product, Order, OrderItem

class TestOnlineShop(unittest.TestCase):

    def setUp(self):
        self.user = User(1, "Alice", "alice@example.com", "password123")
        self.product1 = Product(1, "Laptop", "Gaming laptop", 1200.0, 10)
        self.product2 = Product(2, "Mouse", "Wireless mouse", 50.0, 20)

    def test_register(self):
        self.user.register()
        self.assertEqual(self.user.name, "Alice")

    def test_login_success(self):
        self.assertTrue(self.user.login("alice@example.com", "password123"))

    def test_login_fail(self):
        self.assertFalse(self.user.login("alice@example.com", "wrongpassword"))

    def test_create_order(self):
        order = self.user.create_order()
        self.assertEqual(order.user.name, "Alice")
        self.assertEqual(order.status, "New")

    def test_add_product_to_order(self):
        order = self.user.create_order()
        order.add_product(self.product1, 2)
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.items[0].quantity, 2)

    def test_remove_product_from_order(self):
        order = self.user.create_order()
        order.add_product(self.product1, 2)
        order.remove_product(self.product1)
        self.assertEqual(len(order.items), 0)

    def test_calculate_total(self):
        order = self.user.create_order()
        order.add_product(self.product1, 1)
        order.add_product(self.product2, 2)
        total = order.calculate_total()
        self.assertEqual(total, 1200.0 + 2*50.0)
        
    def test_change_order_status(self):
        order = self.user.create_order()
        order.change_status("Shipped")
        self.assertEqual(order.status, "Shipped")

    def test_update_stock(self):
        self.product1.update_stock(5)
        self.assertEqual(self.product1.stock_quantity, 15)

    def test_order_item_subtotal(self):
        item = OrderItem(self.product2, 3)
        self.assertEqual(item.get_subtotal(), 3 * 50.0)


if __name__ == '__main__':
    unittest.main()
