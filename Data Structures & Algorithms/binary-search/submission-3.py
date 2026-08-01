class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if (len(nums) - 1) == 0 and target == nums[0]:
            return 0
        while l < r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            m = int((l + r) / 2)
            print(f"left index is {l}, right index is {r}")
            print(f"middle index is {m}")
            if nums[m] != target:
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                return m 
        return -1