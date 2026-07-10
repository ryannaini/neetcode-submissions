class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        hashmap = {'}': '{', ']': '[', ')': '('}

        stack = []
        for a in s:
            print(a)
            if a in hashmap.keys(): #if it is },],)
                if len(stack) == 0: ## if its empty return false such case insludes "]" or "[]]"
                    return False
                if hashmap[a] == stack[-1]: #if it equals the most recent stacked item
                    stack.pop()
                else:
                    return False
            else: # '{...
                stack.append(a)
        if stack:
            return False
        return True
    

        