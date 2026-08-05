class PortfolioOptimizer:

    def optimize(self, current, target):

        recommendations = []

        for stock in target:

            difference = target[stock] - current.get(stock, 0)

            recommendations.append({
                "Stock": stock,
                "Adjustment": difference
            })

        return recommendations
