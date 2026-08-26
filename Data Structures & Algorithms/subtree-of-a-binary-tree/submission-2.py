# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## psuedo-code:

## does root exist? and/or subroot exist?, if root DNE but subroot does, return False
## is root exists check if subroot exist
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return False

        if self.isSame(root, subRoot):
            return True


        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    ## And Statement
    def isSame(self, s, t):
        if not t and not s:
            return True
        if t and not s:
            return False
        if s and not t:
            return False
        
        if s.val == t.val:
            return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        return False

        
