class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 

        while l < r: # Don't need to call this function iteratively just need this while loop
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l+1, r+1]

        