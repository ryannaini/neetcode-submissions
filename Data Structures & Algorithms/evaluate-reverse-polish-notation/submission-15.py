class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elt in tokens:
            match elt:
                case '+':
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = first + second 
                    stack.append(res)
                case '*':
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = first * second 
                    stack.append(res)
                case '-':
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = second - first 
                    stack.append(res)
                case '/':
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = int(second / first)
                    stack.append(res)
                case _:
                    stack.append(elt)
        return int(stack[0])
        