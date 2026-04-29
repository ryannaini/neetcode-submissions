class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "#" + word
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #everything before is the length 
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length             
        return res


        

            
            

