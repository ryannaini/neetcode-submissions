class Solution:
    def characterReplacement(self, s, k):
        dic = [0] * 26
        res = 1
        l,r = 0,1
        dic[ord(s[l]) - ord('A')] += 1
        while r < len(s):
            dic[ord(s[r]) - ord('A')] += 1 

            if ((r - l + 1) - max(dic)) <= k:
                res = max(res, (r-l + 1))
            else:
                while ((r - l) + 1) - max(dic) > k:
                    dic[ord(s[l]) - ord('A')] -= 1
                    l += 1
            r += 1
        return res

        