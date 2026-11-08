class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        left = 0
        right = len(heights) - 1
        while left < right:
            distance = right - left
            if heights[left] > heights[right]:
                container = heights[right] * distance
                right -= 1
            else:
                container = heights[left] * distance
                left += 1
            res = max(res, container)
        return res