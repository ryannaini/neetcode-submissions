# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        IsBalanced = True

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal IsBalanced
            if abs(left - right) <= 1 and IsBalanced:
                IsBalanced = True
            else:
                IsBalanced = False
            return 1 + max(left, right)

        dfs(root)
        return IsBalanced
        