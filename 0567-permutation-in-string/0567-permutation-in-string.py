class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if m<n:
            return False
        hp1={}
        hp2={}
        for i in s1:
            hp1[i]=hp1.get(i,0)+1
        for i in range(n):
            hp2[s2[i]]=hp2.get(s2[i],0)+1
        if hp1==hp2:
            return True
        for i in range(n,m):
            hp2[s2[i-n]]-=1
            if hp2[s2[i-n]]==0:
                del hp2[s2[i-n]]
            hp2[s2[i]]=hp2.get(s2[i],0)+1
            if hp1==hp2:
                return True
        return False