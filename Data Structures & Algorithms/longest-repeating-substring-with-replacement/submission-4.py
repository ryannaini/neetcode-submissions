class Solution:
    def characterReplacement(self, s, k):
        count = [0] * 26
        maxFreq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            maxFreq = max(maxFreq, count[idx])   # only grows
            if (r - l + 1) - maxFreq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
        