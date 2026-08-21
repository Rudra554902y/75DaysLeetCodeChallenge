class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # n = len(nums)
        # t = [[-1] * (2) for _ in range(n + 1)]
        # def solve(idx, flag):
        #     if idx >= n:
        #         return 0
        #     if t[idx][flag] != -1:
        #         return t[idx][flag]
        #     skip = solve(idx + 1, flag)

        #     val = nums[idx]

        #     if not flag:
        #         val *= -1
            
        #     take = solve(idx + 1, not flag) + val

        #     t[idx][flag] = max(skip, take)
        #     return t[idx][flag]


        # return solve(0, True)
        n = len(nums)
        t = [[0] * (2) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            t[i][0] = max(t[i - 1][1] - nums[i - 1], t[i - 1][0])
            t[i][1] = max(t[i - 1][0] + nums[i - 1], t[i - 1][1])

        return max(t[n][0], t[n][1])