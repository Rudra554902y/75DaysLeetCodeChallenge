class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=max_=0
        char=set()
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[left])
                left+=1
            char.add(s[r])
            max_=max(max_,r-left+1)
        return max_