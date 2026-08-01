class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        def solve(i, j):
            if i == j:
                return nums[i]

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = max(nums[i] - solve(i + 1, j), nums[j] - solve(i, j - 1))

            return dp[i][j]
        return solve(0, len(nums) - 1) >= 0

