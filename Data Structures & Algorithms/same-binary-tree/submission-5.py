# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        queue = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    queue.append((node1.left, node2.left))
                    queue.append((node1.right, node2.right))
            elif (node1 and not node2) or (not node1 and node2):
                return False
        return True
            