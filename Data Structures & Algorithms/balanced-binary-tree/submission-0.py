# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if abs(height(l) - height(r)) > 1 at any subtree, return false
        self.balanced = True
        
        def getHeight(node):
            if not node:
                return 0
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)

            if abs(left_height - right_height) > 1:
                self.balanced = False

            return 1 + max(left_height, right_height)
        
        getHeight(root)
        return self.balanced
        