class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # dp = [[-1] * (k + 1) for _ in range(n + 1)]
        # def solve(n, k, i):
        #     if k == 0:
        #         return 1
        #     if i >= n:
        #         return 0
        #     if dp[i][k] != -1:
        #         return dp[i][k]
        #     skip = solve(n, k, i + 1) % 1000000007
        #     take = 0
        #     for j in range(i + 1, n):
        #         take = (take + solve(n, k - 1, j)) % 1000000007
        #     dp[i][k] = (skip + take) % 1000000007
        #     return dp[i][k]
        # return solve(n, k, 0)

        mod = 1000000007
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(n):
            dp[0][i] = 1
        for j in range(1,k + 1):
            suffix = [0] * (n + 1)
            for h in range(n - 1, -1, -1):
                suffix[h] = (suffix[h + 1] + dp[j - 1][h]) % mod
            for i in range(n - 1, -1, -1):
                skip = dp[j][i + 1] % mod
                take = suffix[i + 1] % mod
                dp[j][i] = (skip + take) % mod
        return dp[k][0]