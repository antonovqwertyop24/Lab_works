class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to the warehouse.")

    def remove_product(self, product_name):
        product = next((p for p in self.products if p.name == product_name), None)
        if product:
            self.products.remove(product)
            print(f"{product_name} removed from the warehouse.")
        else:
            print(f"Product {product_name} not found.")

    def inventory(self):
        print("Inventory Report:")
        for product in self.products:
            print(product.get_info())

    def find_product(self, product_name):
        return next((p for p in self.products if p.name == product_name), None)
