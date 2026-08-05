class TaxAgent:

    def optimize_tax(self, trades):

        optimized = []

        for trade in trades:

            if trade["Action"] == "SELL":
                trade["Tax_Note"] = "Consider long-term capital gains tax."

            elif trade["Action"] == "BUY":
                trade["Tax_Note"] = "No immediate tax impact."

            else:
                trade["Tax_Note"] = "No action required."

            optimized.append(trade)

        return optimized
