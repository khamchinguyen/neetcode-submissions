class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            s_sort = sorted(s)
            s_sort = tuple(s_sort)
            hashmap[s_sort].append(s)
        return list(hashmap.values())