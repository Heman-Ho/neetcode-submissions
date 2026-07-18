from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Traverse the Tree level by level using a queue
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            level_width = len(q)
            for i in range(level_width):
                node = q.popleft()
                # at each level, append the right most node's value to the result array
                if i == level_width - 1:
                    res.append(node.val)
                # add each node's children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
           
        
        return res