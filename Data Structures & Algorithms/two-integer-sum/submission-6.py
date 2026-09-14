class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = []
        for i, v in enumerate(nums):
            copy.append([v, i])
        copy = sorted(copy)
        i, j = 0, len(copy) - 1
        while i < j:
            if target == copy[i][0] + copy[j][0]:
                return [min(copy[i][1], copy[j][1]), max(copy[i][1], copy[j][1])]
            if target < copy[i][0] + copy[j][0]:
                j -= 1
            if target > copy[i][0] + copy[j][0]:
                i += 1
            