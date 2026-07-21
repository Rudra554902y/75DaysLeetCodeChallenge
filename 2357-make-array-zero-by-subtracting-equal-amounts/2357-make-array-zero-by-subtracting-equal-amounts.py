class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set(nums)
        return sum(i != 0 for i in a)