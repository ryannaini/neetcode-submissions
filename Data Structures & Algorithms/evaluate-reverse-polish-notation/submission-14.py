class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elt in tokens:
            if elt == "+":
                first = int(stack.pop())
                second = int(stack.pop())
                res = first + second 
                stack.append(res)
            elif elt == '*':
                first = int(stack.pop())
                second = int(stack.pop())
                res = first * second 
                stack.append(res)
            elif elt == '-':
                first = int(stack.pop())
                second = int(stack.pop())
                res = second - first 
                stack.append(res)
            elif elt == '/':
                
                first = int(stack.pop())
                second = int(stack.pop())
                res = int(second / first)
                stack.append(res)
            else:
                stack.append(elt)
        return int(stack[0])
        