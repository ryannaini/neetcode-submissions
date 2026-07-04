class Solution:
    def maxArea(self, heights: List[int]) -> int:
        finalArea = 0
        for l, a in enumerate(heights): # l being index and 'a' being actual number
            r = len(heights) - 1 
            while l < r:
                shortest = min(a, heights[r])
                currArea = shortest * len(heights[l:r])
                if finalArea < currArea:
                    finalArea = currArea
                r -= 1 
        return finalArea

