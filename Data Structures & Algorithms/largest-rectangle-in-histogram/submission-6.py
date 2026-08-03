class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        count = 0
        for i,h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                start_idx, stackHeight = stack.pop()
                area = stackHeight * (i - start_idx)
                res = max(area, res)
                start = start_idx
            stack.append((start, h))
        for i,h in stack:
            area = h * (len(heights) - i)
            res = max(area, res)
        return res 