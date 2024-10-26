from core.warehouse import Warehouse
from core.rent_system import RentSystem
from core.product import Product

def main():
    rent_system = RentSystem()
    warehouse = Warehouse(rent_system)

    book = Product(name="Book", quantity=10, price=5.0)
    warehouse.add_product(book)
    print("Inventory:", warehouse.inventory_status())

if __name__ == "__main__":
    main()