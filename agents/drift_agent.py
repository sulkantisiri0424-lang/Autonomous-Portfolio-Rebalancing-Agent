class DriftAgent:
    def __init__(self, threshold=5):
        self.threshold = threshold

    def check_drift(self, current, target):
        results = {}

        for stock in target:
            current_value = current.get(stock, 0)
            target_value = target[stock]

            drift = current_value - target_value

            results[stock] = {
                "Current": current_value,
                "Target": target_value,
                "Drift": drift,
                "Rebalance": abs(drift) >= self.threshold
            }

        return results
