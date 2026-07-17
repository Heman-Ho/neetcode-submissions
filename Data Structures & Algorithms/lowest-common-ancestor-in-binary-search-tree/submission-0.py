# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        LCA = root.val

        # if p and q are both less than current node's val, then the LCA must be in the left subtree
        if p.val < LCA and q.val < LCA:
            return self.lowestCommonAncestor(root.left, p, q)
        # if p and q are both greater than current node's val, then LCA must be in the right subtree
        if p.val > LCA and q.val > LCA:
            return self.lowestCommonAncestor(root.right, p, q)
        # otherwise p and q are in left and right or either one of p and q is the current node and the other is 
        # within the subtree => cur node is the LCA
        return root
        

       