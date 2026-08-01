class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            first_index = m // len(matrix[0])
            second_index = m % len(matrix[0])
            mValue = matrix[first_index][second_index]
            if mValue > target:
                r = m - 1
            elif mValue < target:
                l = m + 1
            else:
                return True
        return False