import yfinance as yf

class MarketAgent:

    def get_stock_price(self, symbol):
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if data.empty:
            return None

        return round(data["Close"].iloc[-1], 2)

    def get_multiple_prices(self, symbols):
        prices = {}

        for symbol in symbols:
            prices[symbol] = self.get_stock_price(symbol)

        return prices
