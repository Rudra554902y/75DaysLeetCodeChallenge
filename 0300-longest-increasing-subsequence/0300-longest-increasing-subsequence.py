class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n=len(nums)
        # dp=[1]*n
        # for i in range(1,n):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return max(dp)
        ls=[nums[0]]
        for i in range(1,len(nums)):
            if ls[-1]<nums[i]:
                ls.append(nums[i])
            else:
                idx=bisect.bisect_left(ls,nums[i])
                ls[idx]=nums[i]
        return len(ls)