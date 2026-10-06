class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## Base Case
        if len(nums) == 0:
            return [[]]
        
        # Make a subarray, and go and recurse upwards
        perms = self.permute(nums[1:])
        res = []

        for p in perms: 
            # go through every possible index we can insert our value
            for i in range(len(p) + 1): # 0 --> len(p), we can add to the end of the permutation
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
