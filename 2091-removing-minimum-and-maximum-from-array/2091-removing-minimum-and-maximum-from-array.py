class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mxi = 0
        mni = 0
        n = len(nums)
        for i in range(1, n):
            if nums[mxi] < nums[i]:
                mxi = i
            if nums[mni] > nums[i]:
                mni = i
        front = min(mxi, mni)
        back = max(mxi, mni)
        return min(back + 1, n - front, front + 1 + (n - back))