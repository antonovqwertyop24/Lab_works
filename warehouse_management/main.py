from product import Book, Electronics, Clothing
from warehouse import Warehouse
from rent_system import RentSystem
from user_system import User

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
            # Добавление товара
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            product_type = input("Enter product type (book/electronics/clothing): ").strip().lower()

            if product_type == "book":
                product = Book(name, quantity, price)
            elif product_type == "electronics":
                product = Electronics(name, quantity, price)
            elif product_type == "clothing":
                product = Clothing(name, quantity, price)
            else:
                print("Invalid product type!")
                continue
            
            warehouse.add_product(product)

        elif choice == '2':
            # Удаление товара
            name = input("Enter product name to remove: ")
            warehouse.remove_product(name)

        elif choice == '3':
            # Показать инвентаризацию
            warehouse.inventory()

        elif choice == '4':
            # Аренда товара
            name = input("Enter product name to rent: ")
            quantity = int(input("Enter quantity to rent: "))
            product = warehouse.find_product(name)

            if product:
                user1.borrow(product, quantity, rent_system)
            else:
                print("Product not found.")

        elif choice == '5':
            # Возврат товара
            name = input("Enter product name to return: ")
            quantity = int(input("Enter quantity to return: "))
            product = warehouse.find_product(name)

            if product:
                user1.return_item(product, quantity, rent_system)
            else:
                print("Product not found.")

        elif choice == '6':
            # Выход из программы
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
