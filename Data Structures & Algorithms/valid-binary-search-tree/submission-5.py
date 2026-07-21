# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            # For any left child node, it's upper limit is directly bound by it's parent's value. 
            # It's lower limit is inherited from it's parent's lower limit.
            # For any right child node, it's lower limit is directly bound by it's parent's value.
            # It's upper limit is inherited from it's parent's upper limit
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root, float('-inf'), float('inf'))

        # stack = []
        # cur = root
        # prev = float('-inf')
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     if cur.val <= prev:
        #         return False
        #     prev = cur.val
        #     cur = cur.right
        # return True
            