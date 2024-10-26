import unittest
from warehouse_management.core.product import Book, Electronics, Clothing
from warehouse_management.core.warehouse import Warehouse
from warehouse_management.core.rent_system import RentSystem
from warehouse_management.core.user_system import User
from main import add_product_to_warehouse, rent_product, return_product

class TestWarehouseSystem(unittest.TestCase):
    def setUp(self):
        self.warehouse = Warehouse()
        self.rent_system = RentSystem()
        self.user = User("Test User")

    def test_add_product(self):
        product = add_product_to_warehouse(self.warehouse, "Test Book", 10, 15.99, "book")
        self.assertIn(product, self.warehouse.products)
        self.assertEqual(product.quantity, 10)

    def test_rent_product(self):
        product = add_product_to_warehouse(self.warehouse, "Test Book", 10, 15.99, "book")
        rent_product(self.warehouse, self.rent_system, self.user, "Test Book", 2)
        self.assertEqual(product.quantity, 8)

    def test_return_product(self):
        product = add_product_to_warehouse(self.warehouse, "Test Book", 10, 15.99, "book")
        rent_product(self.warehouse, self.rent_system, self.user, "Test Book", 2)
        return_product(self.warehouse, self.rent_system, self.user, "Test Book", 2)
        self.assertEqual(product.quantity, 10)

    def test_invalid_product_type(self):
        with self.assertRaises(ValueError):
            add_product_to_warehouse(self.warehouse, "Invalid Product", 10, 15.99, "unknown")

if __name__ == "__main__":
    unittest.main()
