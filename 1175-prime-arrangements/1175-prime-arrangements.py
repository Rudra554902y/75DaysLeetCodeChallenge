class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def fact(n):
            if n==0 or n==1:
                return 1
            f=1
            for i in range(2,n+1):
                f*=i
            return f
        mod=10**9+7
        prime=[True]*(n+1)
        prime[0]=prime[1]=False
        for i in range(2,n+1):
            if prime[i]:
                for j in range(i*i,n+1,i):
                    prime[j]=False
        c=0
        for i in range(n+1):
            if prime[i]:
                c+=1
        return ((fact(c)%mod)*(fact(n-c)%mod))%mod