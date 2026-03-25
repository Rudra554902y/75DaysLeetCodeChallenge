class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[i for i in range(1,n+1)]
        def helper(ds,dset):
            nonlocal k
            if len(ds)==n:
                k-=1
                if k==0:
                    return ds[:]
                return None
            for x in nums:
                if x not in dset:
                    ds.append(x)
                    dset.add(x)
                    res=helper(ds,dset)
                    if res is not None:
                        return res
                    ds.pop()
                    dset.remove(x)
        re=helper([],set())
        s="".join(list(map(str,re)))
        return s