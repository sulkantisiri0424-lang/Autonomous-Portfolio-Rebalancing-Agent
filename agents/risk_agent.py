class RiskAgent:

    def calculate_risk(self, portfolio):

        total = sum(portfolio.values())

        risk = {}

        for stock, value in portfolio.items():

            percentage = (value / total) * 100

            if percentage > 40:
                level = "High"

            elif percentage > 20:
                level = "Medium"

            else:
                level = "Low"

            risk[stock] = {
                "Allocation": round(percentage, 2),
                "Risk": level
            }

        return risk
