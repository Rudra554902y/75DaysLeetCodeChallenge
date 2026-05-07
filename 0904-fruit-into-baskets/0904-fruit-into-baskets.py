class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last = slast = -1
        lastcount = curr = res = 0
        for f in fruits:
            if f == last or f == slast:
                curr += 1
            else:
                curr = lastcount + 1
            if f == last:
                lastcount += 1
            else:
                lastcount = 1
                slast, last = last, f
            res = max(res, curr)
        return res