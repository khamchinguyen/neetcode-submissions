class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            order = [0] * 26
            for c in s:
                order[ord(c) - ord('a')] = order[ord(c) - ord('a')] + 1
            order = tuple(order)
            hashmap[order].append(s)
        return list(hashmap.values())