import unittest
from core.warehouse import Warehouse
from core.product import Product
from core.rent_system import RentSystem

class TestWarehouse(unittest.TestCase):
    def setUp(self):
        self.rent_system = RentSystem()
        self.warehouse = Warehouse(self.rent_system)
        self.product = Product(name="Test Product", quantity=5, price=10.0)
        self.warehouse.add_product(self.product)

    def test_add_product(self):
        self.assertIn(self.product, self.warehouse.inventory)

    def test_remove_product(self):
        self.warehouse.remove_product("Test Product")
        self.assertNotIn(self.product, self.warehouse.inventory)

    def test_inventory_status(self):
        self.assertEqual(self.warehouse.inventory_status(), [("Test Product", 5)])

if __name__ == '__main__':
    unittest.main()