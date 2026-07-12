class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if (i != j) and (i < j) and (prices[i] < prices[j]) and (prices[j] - prices[i] > max_profit):
                    max_profit = prices[j] - prices[i] 
        return max_profit
