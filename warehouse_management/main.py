import argparse
from core.product import Book, Electronics, Clothing
from core.warehouse import Warehouse
from core.rent_system import RentSystem
from core.user_system import User

def main():
    warehouse = Warehouse()
    rent_system = RentSystem()
    user1 = User("John Doe")

    parser = argparse.ArgumentParser(description='Warehouse Management System')
    parser.add_argument('--action', choices=['add', 'remove', 'show', 'rent', 'return', 'exit'], required=True)
    parser.add_argument('--name', type=str)
    parser.add_argument('--quantity', type=int)
    parser.add_argument('--price', type=float)
    parser.add_argument('--type', type=str)

    args = parser.parse_args()

    if args.action == 'add':
        if args.name and args.quantity and args.price and args.type:
            add_product_to_warehouse(warehouse, args.name, args.quantity, args.price, args.type)
        else:
            print("Missing arguments for adding a product.")

    elif args.action == 'remove':
        if args.name:
            warehouse.remove_product(args.name)
        else:
            print("Missing product name.")

    elif args.action == 'show':
        warehouse.inventory()

    elif args.action == 'rent':
        if args.name and args.quantity:
            rent_product(warehouse, rent_system, user1, args.name, args.quantity)
        else:
            print("Missing arguments for renting a product.")

    elif args.action == 'return':
        if args.name and args.quantity:
            return_product(warehouse, rent_system, user1, args.name, args.quantity)
        else:
            print("Missing arguments for returning a product.")

    elif args.action == 'exit':
        print("Exiting program.")

if __name__ == "__main__":
    main()
