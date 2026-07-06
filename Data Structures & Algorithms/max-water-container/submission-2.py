class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        finalArea = 0
        while l < r:
            currArea = len(heights[l:r]) * min(heights[l], heights[r])
            finalArea = max(currArea, finalArea)
            if heights[l] == min(heights[l], heights[r]):
                l += 1 
            else:
                r -= 1
        return finalArea
        