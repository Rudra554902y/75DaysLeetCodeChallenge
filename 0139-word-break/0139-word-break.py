class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m=len(s)
        memo={}
        # @lru_cache(None)
        def helper(idx):
            if idx==m:
                return True
            if idx in memo:
                return memo[idx]
            for word in wordDict:
                i=0
                a=idx
                n=len(word)
                while i<n and a<m and s[a]==word[i]:
                    a+=1
                    i+=1
                if i==n:
                    if helper(idx+n):
                        memo[idx]=True
                        return True
            memo[idx]=False
            return False
        return helper(0)