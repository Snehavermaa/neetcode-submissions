class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lowest=prices[0]
        for i in prices:
            
            max_profit=max(max_profit, i-lowest)
            lowest=min(lowest, i)
        return max_profit
            
        