class Backtesting:

    def run(self, initial_value, final_value):

        profit = final_value - initial_value

        roi = (profit / initial_value) * 100

        return {
            "Initial Value": initial_value,
            "Final Value": final_value,
            "Profit": profit,
            "ROI (%)": round(roi, 2)
        }
