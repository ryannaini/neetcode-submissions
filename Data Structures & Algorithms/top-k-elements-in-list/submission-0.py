class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        result = []
        for number in nums:
            if number in dictionary:
                dictionary[number] += 1
            else: 
                dictionary[number] = 1
        # Now Check the top K Frequent Element(s)
        counter = k 
        while counter > 0:
            max_key = max(dictionary, key = dictionary.get)
            result.append(max_key)
            counter = counter - 1
            dictionary.pop(max_key)
        return result
                
        
        