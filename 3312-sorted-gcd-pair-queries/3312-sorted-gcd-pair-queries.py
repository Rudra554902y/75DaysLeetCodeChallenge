class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # frequency of each number
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = pairs whose gcd is exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2
            for multiple in range(2 * d, mx + 1, d):
                pairs -= exact[multiple]
            exact[d] = pairs

        values = []
        prefix = []

        total = 0
        for d in range(1, mx + 1):
            if exact[d]:
                total += exact[d]
                values.append(d)
                prefix.append(total)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans