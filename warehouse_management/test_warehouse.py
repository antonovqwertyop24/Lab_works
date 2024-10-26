import unittest
from unittest.mock import MagicMock, patch
from core.warehouse import Warehouse
from core.product import Product
from core.rent_system import RentSystem

class TestWarehouse(unittest.TestCase):
    def setUp(self):
        # Створюємо мок для RentSystem
        self.rent_system = MagicMock(spec=RentSystem)
        
        # Створюємо екземпляр Warehouse з мокованим RentSystem
        self.warehouse = Warehouse(self.rent_system)
        self.product = Product(name="Test Product", quantity=5, price=10.0)
        
        # Додаємо продукт до складу
        self.warehouse.add_product(self.product)

    def test_add_product(self):
        self.assertIn(self.product, self.warehouse.inventory)

    def test_remove_product(self):
        self.warehouse.remove_product("Test Product")
        self.assertNotIn(self.product, self.warehouse.inventory)

    def test_inventory_status(self):
        self.assertEqual(self.warehouse.inventory_status(), [("Test Product", 5)])

    def test_rent_item(self):
        # Налаштовуємо мок для rent_item
        self.rent_system.rent_item = MagicMock()

        # Викликаємо метод rent_item через Warehouse
        self.warehouse.rent_system.rent_item(self.product, 2)

        # Перевіряємо, чи був викликаний метод rent_item
        self.rent_system.rent_item.assert_called_once_with(self.product, 2)

    def test_return_item(self):
        # Налаштовуємо мок для return_item
        self.rent_system.return_item = MagicMock()

        # Викликаємо метод return_item через Warehouse
        self.warehouse.rent_system.return_item(self.product, 2)

        # Перевіряємо, чи був викликаний метод return_item
        self.rent_system.return_item.assert_called_once_with(self.product, 2)

if __name__ == '__main__':
    unittest.main()
