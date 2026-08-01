class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i,h in enumerate(heights):
            l,r = i,i
            while True:
                if (r + 1) < len(heights):
                    test = r + 1
                    if heights[test] >= heights[i]:
                        r = test
                        continue
                    break
                else:
                    break
            while True:
                if (l - 1) in range(len(heights)):
                    test = l - 1
                    if heights[test] >= heights[i]:
                        l = test
                        continue
                    break
                else:
                    break
            rectangle_height = h * (r - l + 1)
            res = max(res, rectangle_height)
        return res