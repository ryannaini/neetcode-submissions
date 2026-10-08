class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        s = {()}

        for n in nums:
            new = set()
            for t in s:
                new.add(t + (n,))
            s |= new # Union
        return [list(t) for t in s]
               

