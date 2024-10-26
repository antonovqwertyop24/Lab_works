class RentSystem:
    def __init__(self):
        self.rented_items = []

    def rent_item(self, product, quantity):
        if product.quantity >= quantity:
            product.remove_quantity(quantity)
            self.rented_items.append((product, quantity))
            print(f"Rented {quantity} of {product.name}")
        else:
            print(f"Not enough {product.name} in stock for renting.")

    def return_item(self, product, quantity):
        rented_product = next((p for p in self.rented_items if p[0] == product), None)
        if rented_product:
            self.rented_items.remove(rented_product)
            product.add_quantity(quantity)
            print(f"Returned {quantity} of {product.name}")
        else:
            print(f"{product.name} not found in rented items.")
