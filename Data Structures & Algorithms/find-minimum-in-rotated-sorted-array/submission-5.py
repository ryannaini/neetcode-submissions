class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                res = min(nums[l], res)
                l = m + 1 
            else:
                res = min(nums[m], res)
                r = m - 1
        return res

            
        