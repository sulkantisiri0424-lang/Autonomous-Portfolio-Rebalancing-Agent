class ExplanationAgent:

    def explain(self, trades):

        explanations = []

        for trade in trades:

            if trade["Action"] == "BUY":
                message = f"Buy {trade['Stock']} because it is below the target allocation."

            elif trade["Action"] == "SELL":
                message = f"Sell {trade['Stock']} because it exceeds the target allocation."

            else:
                message = f"No action required for {trade['Stock']}."

            explanations.append({
                "Stock": trade["Stock"],
                "Explanation": message
            })

        return explanations
