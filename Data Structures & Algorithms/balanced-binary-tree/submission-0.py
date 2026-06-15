# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            
            lHeight = dfs(root.left)
            
            rHeight = dfs(root.right)
            if lHeight == -1:
                return -1
            elif rHeight == -1:
                return -1
            elif abs(lHeight-rHeight) > 1:
                return -1
            
            return max(lHeight, rHeight) + 1
        
        x = dfs(root)

        if x == -1:
            return False
        else:
            return True