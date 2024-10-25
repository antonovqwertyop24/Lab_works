class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow(self, product, quantity, rent_system):
        rent_system.rent_item(product, quantity)
        self.borrowed_items.append((product, quantity))

    def return_item(self, product, quantity, rent_system):
        rent_system.return_item(product, quantity)
        self.borrowed_items.remove((product, quantity))
