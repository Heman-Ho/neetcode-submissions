# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        # We do a dfs keeping track of the largest val in the path so far using the recursive stack
        def dfs(node, largest):
            nonlocal res
            # base case 
            if not node:
                return
            if node.val >= largest:
                res += 1
                largest = node.val
            dfs(node.left, largest)
            dfs(node.right, largest)
        
        dfs(root, root.val - 1)
        return res
        