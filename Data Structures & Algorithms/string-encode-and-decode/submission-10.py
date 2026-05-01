class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "#" + word
        return res 
    
    def decode(self, s: str ) -> List[str]:
        res = []
        i = 0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
                continue
            if s[j] == "#":
                length_of_word = s[i:j]
                res.append(s[j+1 : j + 1 + int(length_of_word)])
            i = j + 1 + int(length_of_word)
            print(i)
        return res 
 

        

            
            

