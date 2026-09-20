class Solution:
    def reverseDegree(self, s: str) -> int:
        sm = 0
        for i in range(len(s)):
            r_idx = ord('z') - ord(s[i]) + 1
            sm += r_idx * (i + 1)
        return sm