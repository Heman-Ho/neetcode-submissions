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

        # We do a dfs keeping track of the largest val in the path so far using the recursive stack
        def dfs(node, largest):
            # base case 
            if not node:
                return 0
            isGood = 1 if node.val >= largest else 0
            largest = max(largest, node.val)
 
            return isGood + dfs(node.left, largest) + dfs(node.right, largest)
       
        return dfs(root, root.val)
 
        