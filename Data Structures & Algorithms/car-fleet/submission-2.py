class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[position[i], speed[i]] for i in range(len(position))]

        stack = []
        for p,s in sorted(pair)[::-1]:
            if stack:
                time = (target - p) / s
                if time > stack[-1]:
                    stack.append(time)
            else:
                time = (target - p) / s
                stack.append(time)
        return len(stack)