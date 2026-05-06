class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr=0
        mn=float('inf')
        for right in range(n):
            curr+=nums[right]
            while curr>=target:
                mn = min(mn,right-left+1)
                curr-=nums[left]
                left+=1
        return mn if mn!=float('inf') else 0