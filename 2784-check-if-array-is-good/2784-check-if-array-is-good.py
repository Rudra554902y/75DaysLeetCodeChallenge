class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        m=len(nums)
        if m!=n+1:
            return False
        nums.sort()
        for i in range(1,n):
            if nums[i-1]!=i:
                return False
        return nums[-1]==n and nums[-2]==n