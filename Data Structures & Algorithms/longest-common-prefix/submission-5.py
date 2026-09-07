class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
    
        for s in strs[0]:
            res += (s)

            
        
        for string in strs[1:]:
            if len(string) == 0:
                return ""
            for i in range(len(string)):
                letter_1 = res[i] if (i < len(res)) else 'A'
                letter_2 = string[i] if (i < len(string)) else 'A'
                
                print(letter_1, letter_2)
                if letter_1 != letter_2:
                    res = res[:i]
                    print(f"res is {res}")
                res = res[:len(string)] 
            print("\n")
        return res