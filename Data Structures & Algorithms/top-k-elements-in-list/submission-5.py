class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        bucket_sort = [[] for i in range(len(nums) + 1)]
        for n, frequency in hashmap.items():
            bucket_sort[frequency].append(n)
        for n in range(len(nums), 0, -1):
            for num in bucket_sort[n]:
                result.append(num)
                if len(result) >= k:
                    return result

        