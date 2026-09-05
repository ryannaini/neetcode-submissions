class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                res = stack[-1] + a

                if res < 0:
                    stack.pop()

                elif res == 0:
                    stack.pop()
                    a = 0
                else:
                    a = 0
            if a != 0:
                stack.append(a)
        return stack



