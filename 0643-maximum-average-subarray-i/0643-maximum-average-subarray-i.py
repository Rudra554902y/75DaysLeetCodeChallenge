class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        mx=s
        for i in range(k,len(nums)):
            s-=nums[i-k]
            s+=nums[i]
            mx=max(mx,s)
        return mx/k
