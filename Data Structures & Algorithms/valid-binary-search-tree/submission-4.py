# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def validate(node, low, high):
        #     if not node:
        #         return True
        #     if node.val <= low or node.val >= high:
        #         return False

        #     return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        # return validate(root, float('-inf'), float('inf'))
        stack = []
        cur = root
        prev = float('-inf')
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= prev:
                return False
            prev = cur.val
            cur = cur.right
        return True
            