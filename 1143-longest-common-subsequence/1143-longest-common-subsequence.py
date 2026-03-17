class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        memo={}
        def helper(i,j):
            if i==-1 or j==-1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i,j)] = 1+helper(i-1,j-1)
            else:
                memo[(i,j)] = max(helper(i-1,j),helper(i,j-1))
            return memo[(i,j)]
        return helper(n-1,m-1)