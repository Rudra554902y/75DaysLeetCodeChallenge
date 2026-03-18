class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        suffix=[0]*n
        suffix[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]
        pre=1
        result=[0]*n
        for i in range(n):
            result[i]=pre*(suffix[i+1] if i+1<n else 1)
            pre*=nums[i]
        return result