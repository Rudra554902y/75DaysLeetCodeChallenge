class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ml = 0
        hp = {}
        left = 0
        for right in range(n):
            hp[nums[right]] = hp.get(nums[right], 0) + 1
            while hp[nums[right]] > k:
                hp[nums[left]] -= 1
                if hp[nums[left]] == 0:
                    del hp[nums[left]]
                left += 1
            ml = max(ml, right - left + 1)
        return ml