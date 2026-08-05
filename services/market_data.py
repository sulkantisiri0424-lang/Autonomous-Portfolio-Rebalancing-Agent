import yfinance as yf

class MarketData:

    def get_price(self, symbol):
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if data.empty:
            return None

        return float(data["Close"].iloc[-1])

    def get_prices(self, symbols):
        prices = {}

        for symbol in symbols:
            prices[symbol] = self.get_price(symbol)

        return prices
