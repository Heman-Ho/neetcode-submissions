# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We can do an inorder traversal in O(k) to find the kth smallest value 
        stack = [root]
        count = 0
        while stack:
            while stack[-1].left:
                stack.append(stack[-1].left)
                stack[-2].left = None
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            if node.right:
                stack.append(node.right)
                node.right = None
        

            

        
