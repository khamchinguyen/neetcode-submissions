class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        min_heap = []
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        for key, value in hashmap.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [number for frequency, number in min_heap]
