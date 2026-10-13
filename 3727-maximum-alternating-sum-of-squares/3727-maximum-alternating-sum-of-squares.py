class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 2
        arr = sorted(x * x for x in nums)
        return sum(arr[k:]) - sum(arr[:k])