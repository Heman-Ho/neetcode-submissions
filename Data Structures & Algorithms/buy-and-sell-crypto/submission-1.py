class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 
        lowest = prices[0]

        for price in prices:
            best = max(best, price - lowest)
            lowest = min(lowest, price)
        
        return best