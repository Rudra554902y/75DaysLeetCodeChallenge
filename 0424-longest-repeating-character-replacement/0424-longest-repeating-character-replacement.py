class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        maxlen = 0
        mf = 0
        freq = [0] * 26
        for r in range(n):
            idx = ord(s[r]) - ord('A')
            freq[idx] += 1
            mf = max(mf, freq[idx])
            while (r - l + 1 - mf) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen