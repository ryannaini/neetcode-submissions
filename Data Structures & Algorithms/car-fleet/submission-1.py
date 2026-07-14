class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[position[i], speed[i]] for i in range(len(position))]

        stack = []
        for p,s in sorted(pair, reverse=True): ## Most important thing is that because they are in one line, the stack works there is no overpassing and therefore position1 with 100 minles an hour cannot overpass position 5 at 3 miles an hour
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)