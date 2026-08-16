class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # phase 1, Floyd's agorithm

        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        # Create a second slow pointer, and move both slow pointers until they intersect

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow