import unittest
from datetime import datetime
from models import User, Product, Order, OrderItem

class TestOnlineShopInteraction(unittest.TestCase):

    def setUp(self):
        self.user = User(1, "Bob", "bob@example.com", "secret")
        self.product1 = Product(1, "Keyboard", "Mechanical keyboard", 100.0, 5)
        self.product2 = Product(2, "Monitor", "24 inch monitor", 200.0, 2)

    def test_order_linked_to_user(self):
        order = self.user.create_order()
        order.add_product(self.product1, 1)
        order.add_product(self.product2, 2)
        self.assertIn(order, self.user.orders)
        self.assertEqual(len(order.items), 2)
        self.assertEqual(order.items[0].product.name, "Keyboard")
        self.assertEqual(order.items[1].product.name, "Monitor")

    def test_order_exceed_stock(self):
        order = self.user.create_order()
        with self.assertRaises(ValueError):
            order.add_product(self.product2, 5)

    def test_multiple_orders(self):
        order1 = self.user.create_order()
        order2 = self.user.create_order()
        self.assertEqual(len(self.user.orders), 2)
        self.assertNotEqual(order1.id, order2.id)

    def test_remove_product_from_empty_order(self):
        order = self.user.create_order()
        order.remove_product(self.product1)
        self.assertEqual(len(order.items), 0)  

    def test_add_multiple_quantity_same_product(self):
        order = self.user.create_order()
        order.add_product(self.product1, 2)
        order.add_product(self.product1, 3)
        self.assertEqual(len(order.items), 2)
        total_quantity = sum(item.quantity for item in order.items if item.product.id == self.product1.id)
        self.assertEqual(total_quantity, 5)


if __name__ == '__main__':
    unittest.main()
