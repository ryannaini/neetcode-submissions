class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # pair of elements, the index of the height
        for i, h in enumerate(heights):
            start_idx = i 
            # While there is a stack + the latest height in stack > current height
            while stack and stack[-1][1] > h:  
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start_idx = index
            stack.append((start_idx, h))
        for i,h in stack:
            res = max(res, h * (len(heights) - i))
        return res