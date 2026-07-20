# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Do an in-order traversal of the entire BST: 
        # visit left, cur, then right
        # Keep track of the previously visited node. The cur node must be > than the prev
        self.inorder_list = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.inorder_list.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        for i in range(1, len(self.inorder_list)):
            if self.inorder_list[i] <= self.inorder_list[i-1]:
                return False
        return True 
        
        
        