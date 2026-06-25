class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1
                if cnt > (j - i + 1)//2:
                    c += 1
        return c