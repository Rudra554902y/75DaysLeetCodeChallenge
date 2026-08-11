class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        a = set(nums)
        n = len(nums)
        s = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break
        while s in a:
            s += 1
        return s