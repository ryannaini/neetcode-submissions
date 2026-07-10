class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        hashmap = {'}': '{', ']': '[', ')': '('}

        stack = []
        for i in range(len(s)): # Range len(numbers) gives us 0->8 index for length 9
            elt = s[i]
            print(elt)
            if elt in ['(',"{","["]:
                stack.append(elt)
                continue
            
            key = hashmap[elt]
            if not stack:
                return False
            else:
                pop = stack.pop()
            if elt == ')' and key != pop:
                return False
            elif elt == ']' and key != pop:
                return False
            elif elt == '}' and key != pop:
                return False
            else:
                continue
        if stack:
            return False
        return True

        