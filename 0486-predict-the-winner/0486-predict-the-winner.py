class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # n = len(nums)
        # dp = [[-1] * n for _ in range(n)]
        # def solve(i, j):
        #     if i == j:
        #         return nums[i]

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     dp[i][j] = max(nums[i] - solve(i + 1, j), nums[j] - solve(i, j - 1))

        #     return dp[i][j]
        # return solve(0, len(nums) - 1) >= 0

        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                takeLeft = nums[i] - dp[i + 1][j]
                takeRight = nums[j] - dp[i][j - 1]
                dp[i][j] = max(takeLeft, takeRight)
        return dp[0][n-1] >= 0

