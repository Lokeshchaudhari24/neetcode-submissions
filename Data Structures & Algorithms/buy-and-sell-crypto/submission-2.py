class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        profit=0
        maxs=0
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
            elif prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxs=max(maxs,profit)
            r+=1
        return maxs      