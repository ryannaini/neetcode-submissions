from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        nums_s = Counter(s).items()
        nums_t = Counter(t).items()
        for x,y in nums_s:
            found = False
            for a,b in nums_t:
                if x == a and y == b:
                    found = True
                    break
            if not found:
                return False
        return True 