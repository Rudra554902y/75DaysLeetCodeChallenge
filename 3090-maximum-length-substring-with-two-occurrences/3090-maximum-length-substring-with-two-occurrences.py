class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hp = {}
        n = len(s)
        left = 0
        ml = 0
        for i in range(n):
            hp[s[i]] = hp.get(s[i], 0) + 1
            while hp[s[i]] > 2:
                hp[s[left]] -= 1
                if hp[s[left]] == 0:
                    del hp[s[left]]
                left += 1
            ml = max(ml, i - left + 1)
        return ml