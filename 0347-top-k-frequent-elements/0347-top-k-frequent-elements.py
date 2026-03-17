class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp={}
        for i in nums:
            hp[i]=hp.get(i,0)+1
        heap=[]
        for i in hp:
            heapq.heappush(heap,(-hp[i],i))
        res=[]
        while len(res)<k:
            res.append(heapq.heappop(heap)[1])
        return res