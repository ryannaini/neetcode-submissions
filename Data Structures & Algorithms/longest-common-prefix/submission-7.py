class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
    
        for i in range(len(strs[0])): # Arbitrarily using the first for the shortest string
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: ## checks the first condition
                    return res
            res += strs[0][i]
        return res
                