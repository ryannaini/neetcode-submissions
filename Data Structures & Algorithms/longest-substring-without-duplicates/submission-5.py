class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        array = set()

        l, r = 0, 0
        if len(s) == 0:
            return 0
        while r < len(s):
            if s[r] not in array:
                array.add(s[r])
                res = max(res, len(array))
                
            else:
                while True:
                    if s[r] in array:
                        array.remove(s[l])
                        l += 1
                    else:
                        array.add(s[r])
                        break
            r += 1
        return res
