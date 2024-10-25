from product import Book, Electronics, Clothing
from warehouse import Warehouse
from rent_system import RentSystem
from user_system import User

def add_product_to_warehouse(warehouse, name, quantity, price, product_type):
    if product_type == "book":
        product = Book(name, quantity, price)
    elif product_type == "electronics":
        product = Electronics(name, quantity, price)
    elif product_type == "clothing":
        product = Clothing(name, quantity, price)
    else:
        raise ValueError("Invalid product type")
    
    warehouse.add_product(product)
    return product

def rent_product(warehouse, rent_system, user, product_name, quantity):
    product = warehouse.find_product(product_name)
    if product:
        user.borrow(product, quantity, rent_system)
    else:
        print("Product not found.")
    return product

def return_product(warehouse, rent_system, user, product_name, quantity):
    product = warehouse.find_product(product_name)
    if product:
        user.return_item(product, quantity, rent_system)
    else:
        print("Product not found.")
    return product

def main():
    warehouse = Warehouse()
    rent_system = RentSystem()
    user1 = User("John Doe")

    while True:
        print("\n1. Add Product")
        print("2. Remove Product")
        print("3. Show Inventory")
        print("4. Rent Product")
        print("5. Return Product")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            product_type = input("Enter product type (book/electronics/clothing): ").strip().lower()
            add_product_to_warehouse(warehouse, name, quantity, price, product_type)

        elif choice == '2':
            name = input("Enter product name to remove: ")
            warehouse.remove_product(name)

        elif choice == '3':
            warehouse.inventory()

        elif choice == '4':
            name = input("Enter product name to rent: ")
            quantity = int(input("Enter quantity to rent: "))
            rent_product(warehouse, rent_system, user1, name, quantity)

        elif choice == '5':
            name = input("Enter product name to return: ")
            quantity = int(input("Enter quantity to return: "))
            return_product(warehouse, rent_system, user1, name, quantity)

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
