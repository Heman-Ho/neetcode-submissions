# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Calculate the diameter of each subtree by adding the 2 + depth(left) + depth(right)
    
        self.max_diameter = 0

        def longest_path(node):
            if not node: 
                return 0
        
            height_l = longest_path(node.left)
            height_r = longest_path(node.right)
            self.max_diameter = max(height_l + height_r, self.max_diameter)

            return 1 + max(height_l, height_r)

        longest_path(root)
        return self.max_diameter 
