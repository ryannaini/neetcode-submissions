class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            print(i)
            if s[i] in ['{','[','(']:
                stack.append(s[i])
                print(stack)
            elif stack:
                item = stack.pop()
                if s[i] == '}':
                    if item != '{':
                        return False
                elif s[i] == '}':
                    if item != '{':
                        return False
                elif s[i] == ']':
                    if item != '[':
                        return False
                elif s[i] == ')':
                    if item != '(':
                        return False
            else:
                return False
        if stack:
            return False
        else:
            return True

        