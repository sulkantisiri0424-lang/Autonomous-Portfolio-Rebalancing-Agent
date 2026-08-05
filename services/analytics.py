class Analytics:

    def portfolio_summary(self, portfolio):

        total = sum(portfolio.values())

        summary = {
            "Total Value": total,
            "Number of Assets": len(portfolio),
            "Average Allocation": round(total / len(portfolio), 2)
        }

        return summary
