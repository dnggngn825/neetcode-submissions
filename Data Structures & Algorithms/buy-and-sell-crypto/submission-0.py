class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = float('-inf')

        for p in prices:
            sell = max(sell, p-buy)
            if (p < buy):
                buy = p
        
        return max(0, sell)