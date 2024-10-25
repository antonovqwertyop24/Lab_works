class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_quantity(self, amount):
        self.quantity += amount

    def remove_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount

    def get_info(self):
        return f"Product: {self.name}, Quantity: {self.quantity}, Price: {self.price:.2f}"

class Book(Product):
    pass

class Electronics(Product):
    pass

class Clothing(Product):
    pass
