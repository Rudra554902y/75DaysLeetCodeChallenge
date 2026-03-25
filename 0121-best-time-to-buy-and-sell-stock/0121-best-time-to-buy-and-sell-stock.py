class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mx=[-1]*n
        mx[-1]=prices[-1]
        for i in range(n-2,-1,-1):
            mx[i]=max(prices[i],mx[i+1])
        m=-1
        for i in range(n):
            m=max(m,mx[i]-prices[i])
        return m