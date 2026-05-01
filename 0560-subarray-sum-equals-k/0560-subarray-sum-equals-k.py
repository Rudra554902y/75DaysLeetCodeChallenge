class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        hp={0:1}
        pre=0
        for i in nums:
            pre+=i
            if pre-k in hp:
                c+=hp[pre-k]
            hp[pre]=hp.get(pre,0)+1
        return c