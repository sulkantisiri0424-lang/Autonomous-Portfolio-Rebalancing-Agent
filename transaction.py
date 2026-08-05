class Transaction:

    def __init__(self, stock, action, quantity):
        self.stock = stock
        self.action = action
        self.quantity = quantity

    def details(self):
        return {
            "Stock": self.stock,
            "Action": self.action,
            "Quantity": self.quantity
        }
