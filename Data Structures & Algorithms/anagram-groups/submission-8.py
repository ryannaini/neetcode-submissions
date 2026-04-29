class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        res = []
        for word in strs:
            key = "".join(sorted(word))
            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]
        for key in dictionary:
            res.append(dictionary[key])
        return res 
        
            
            

        