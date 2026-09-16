class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= k:
            s = set()
            for elt in nums:
                if elt in s:
                    return True
                s.add(elt)
            return False
    
        else:
            l,r = 0, k
            s = set()
            for i in range(r + 1):
                if nums[i] in s:
                    return True
                s.add(nums[i])
                
            while r != len(nums) - 1:
                s.remove(nums[l])
                l += 1
                if nums[r + 1] in s:
                    return True
                r += 1
                s.add(nums[r])
                
                
            return False