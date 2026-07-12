class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for curr in tokens:
            if (curr == "+"):
                elt1 = int(stack.pop())
                elt2 = int(stack.pop())
                res = elt2 + elt1
                stack.append(res)
                continue
            elif (curr == "*"):
                elt1 = int(stack.pop())
                elt2 = int(stack.pop())
                res = elt2 * elt1
                stack.append(res)
                continue
            elif (curr == "/"):
                elt1 = int(stack.pop())
                elt2 = int(stack.pop())
                res = int(elt2 / elt1)
                stack.append(res)
                continue
            elif (curr == '-'): ## Subtract
                elt1 = int(stack.pop())
                elt2 = int(stack.pop())
                res = elt2 - elt1
                stack.append(res)
                continue
            else:
                stack.append(int(curr))
        return stack.pop()
        