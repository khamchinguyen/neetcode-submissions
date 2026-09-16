class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        arr = [(v, k) for (k, v) in hashmap.items()]
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
