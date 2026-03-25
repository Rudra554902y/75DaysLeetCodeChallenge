class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        pr=0
        for i in range(1,len(prices)):
            if prices[i]<b:
                b=prices[i]
            elif prices[i]-b>pr:
                pr=prices[i]-b
        return pr