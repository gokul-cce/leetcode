class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit,prices[i]-buy)
            buy = min(buy,prices[i])
        return profit

