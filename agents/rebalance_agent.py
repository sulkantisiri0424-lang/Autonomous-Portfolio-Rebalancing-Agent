class RebalanceAgent:

    def generate_trades(self, current, target):
        trades = []

        for stock in target:

            current_value = current.get(stock, 0)
            target_value = target[stock]

            difference = target_value - current_value

            if difference > 0:
                action = "BUY"

            elif difference < 0:
                action = "SELL"

            else:
                action = "HOLD"

            trades.append({
                "Stock": stock,
                "Action": action,
                "Difference": round(abs(difference), 2)
            })

        return trades
