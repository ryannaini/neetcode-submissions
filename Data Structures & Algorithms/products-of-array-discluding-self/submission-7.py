class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #making it the length of nums
        i = 1
        while i < len(nums):
            res[i] *= nums[i-1] * res[i-1]
            i += 1

        postfix = 1 
        for j in range(len(nums) -1, -1, -1): 
            res[j] *= postfix
            postfix *= nums[j]
        return res
        
            


