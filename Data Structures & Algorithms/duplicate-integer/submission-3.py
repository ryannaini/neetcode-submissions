class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []
        for x in nums:
            if x in new_list:
                return True
            else:
                new_list.append(x)
        return False