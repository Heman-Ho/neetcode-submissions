# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deq = deque()
        deq.append(root)
        res = []

        # add all children nodes from the deque to cur_level
        while deq:
            cur_level = []
            level_width = len(deq)
            for i in range(level_width):
                node = deq.popleft()
                cur_level.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(cur_level.copy())
        return res



