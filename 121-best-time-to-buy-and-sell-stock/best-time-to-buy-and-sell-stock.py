class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buying=prices[0]
        profit=0
        for x in prices:
            buying=min(buying, x)
            profit=max(profit, x-buying)
        return profit    

        