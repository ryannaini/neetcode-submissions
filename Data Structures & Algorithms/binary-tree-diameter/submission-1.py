# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(curr):
            ## If we have reached a Null node, return zero
            if not curr:
                return 0

            ## We have a valid node, therefore before we extract and return up,
            ## we need to check all left/right nodes

            left = dfs(curr.left)
            right = dfs(curr.right)

            ## Although intuitively you don't want to have the res be above the returning 
            ## of the Null's, we do need it before it returns up, because dfs(root) needs
            ## to have a complete update of res before it returns up

            nonlocal res
            res = max(res, left + right) ## We are not counting it's own node for diameter
            ## Now we need choose, which one is deeper and then add one and come up
            return max(left, right) + 1 

        dfs(root)
        return res

    