class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            num=0
            while n>0:
                d=n%10
                num=num*10+d
                n//=10
            return num
        return abs(n-reverse(n))