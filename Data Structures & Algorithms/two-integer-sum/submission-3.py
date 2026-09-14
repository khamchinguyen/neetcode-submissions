class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_key_mapping = {}
        for i, v in enumerate(nums):
            needed_number = target - v
            if needed_number in value_key_mapping:
                return [value_key_mapping[needed_number], i]
            value_key_mapping[v] = i