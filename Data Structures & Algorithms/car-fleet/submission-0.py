class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[position[i],speed[i]] for i in range(len(position))]
        
        stack = []
        for p, s in sorted(pair, reverse=True): #Reverse Sorted Order, this sorts it (based on the first position ) 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #That means they collide
                stack.pop()
        return len(stack)