class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i # moves with i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # string goes from i to j integer pointer 4#, = 0,1 s[0:1] = 4
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length 
        return res

            
            

