class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hp=defaultdict(list)
        for i in strs:
            k="".join(sorted(i))
            hp[k].append(i)
        return list(hp.values())