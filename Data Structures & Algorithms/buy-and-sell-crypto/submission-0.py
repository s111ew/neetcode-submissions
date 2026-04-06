class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        lowest = 101
        for price in prices:
            lowest = min(lowest, price)
            profit = price - lowest
            max_profit = max(max_profit, profit)
        return max_profit


        
