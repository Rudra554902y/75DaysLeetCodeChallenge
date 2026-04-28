class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me=nums[0]
        c=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]!=me:
                c-=1
                if c==0:
                    me=nums[i]
                    c=1
            else:
                c+=1
        return me