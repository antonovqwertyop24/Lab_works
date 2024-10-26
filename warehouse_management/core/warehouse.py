from .product import Product
from .rent_system import RentSystem

class Warehouse:
    def __init__(self, rent_system: RentSystem):
        self.rent_system = rent_system
        self.inventory = []

    def add_product(self, product: Product):
        self.inventory.append(product)
        print(f"{product.name} added to the warehouse.")

    def remove_product(self, name: str):
        self.inventory = [p for p in self.inventory if p.name != name]
        print(f"{name} removed from the warehouse.")

    def inventory_status(self):
        return [(p.name, p.quantity) for p in self.inventory]

    def find_product(self, name: str):
        return next((p for p in self.inventory if p.name == name), None)