class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 
        lowest = prices[0]

        for price in prices:
            if price - lowest > best:
                best = price - lowest
            else:
                lowest = min(lowest, price)
        
        return best