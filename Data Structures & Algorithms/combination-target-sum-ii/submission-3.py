class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()

        def dfs(i, curr, total):
            # 1st Base Case, does our list sum to the target?
            if total == target: 
                res.append(curr.copy())
                return
            # 2nd Base Case, can we no longer index a value or reached a total > target

            if i > (len(candidates) - 1) or total > target:
                return

            # include candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            
            # skip candidates[i]
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)
            return
        dfs(0, [], 0)
        return res