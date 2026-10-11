class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                c += nums[i] ** 2
        return c