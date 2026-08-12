class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(position[i], speed[i]) for i in range(len(position))]
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            if stack:
                if ((target - p) / s) > stack[-1]:
                    stack.append((target - p) / s)
            else:
                stack.append((target - p) / s)
        return len(stack)