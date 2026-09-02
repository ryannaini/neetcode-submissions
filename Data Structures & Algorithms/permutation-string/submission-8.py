class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Initialize 2 hash maps

        s1Count = [0] * 26
        s2Count = [0] * 26

        # 1st Loop, go through length of s1 with and add to the dictionary while also 
        # adding to s2 dictionary 

        for i in range(len(s1)):
            idx_s1_hash = ord(s1[i]) - ord('a')
            s1Count[idx_s1_hash] += 1

            idx_s2_hash = ord(s2[i]) - ord('a')
            s2Count[idx_s2_hash] += 1

        # 2nd Loop, go through both hashmaps and find what matches is right now

        matches = 0

        for i in range(26):
            if s1Count[i] == s2Count[i]:  
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')

            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            if s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            if s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1         
        return matches == 26
