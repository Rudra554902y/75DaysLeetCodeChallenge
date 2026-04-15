class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        mn=float('inf')
        n=len(words)
        for i,val in enumerate(words):
            if val==target:
                mn=min(mn,abs(i-startIndex),n-abs(i-startIndex))
        return mn if mn!=float('inf') else -1