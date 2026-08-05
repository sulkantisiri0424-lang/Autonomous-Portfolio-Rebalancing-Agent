class Portfolio:

    def __init__(self):
        self.assets = {}

    def add_asset(self, stock, amount):
        self.assets[stock] = amount

    def get_assets(self):
        return self.assets

    def total_value(self):
        return sum(self.assets.values())
