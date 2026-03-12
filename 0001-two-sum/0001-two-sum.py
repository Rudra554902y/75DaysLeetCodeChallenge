class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,v in enumerate(nums):
            t=target-v
            if t in hashmap:
                return [hashmap[t],i]
            hashmap[v]=i