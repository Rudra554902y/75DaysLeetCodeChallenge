class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow,fast=1,1
        n=len(nums)
        k=1
        while fast<n:
            if nums[fast]==nums[fast-1]:
                fast+=1
                continue
            nums[slow]=nums[fast]
            slow+=1
            fast+=1
            k+=1
        return k
        
