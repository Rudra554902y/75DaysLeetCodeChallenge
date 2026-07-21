class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(i != 0 for i in set(nums))