class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(n):
            num=0
            while n>0:
                digit=n%10
                n//=10
                num=num*10+digit
            return num
        hp={}
        mn=float('inf')
        for i,val in enumerate(nums):
            rev=reverse(val)
            if val in hp:
                mn=min(mn,abs(i-hp[val]))
                hp[val]=i
            hp[rev]=i
        return mn if mn!=float('inf') else -1