# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #    4
        #  2   6
        # 1 3  5 7

        # inorder: 1,2,3,4,5,6,
        # preorder: 4,2,1,3,6,5,

        # The first value in preorder is the root of it's tree
        # in the inorder list, the root partitions the array of it's subtrees
        
        # We need a val to index mapping of the inorder array to achieve O(1) lookup
        val_to_i = {}
        for i, val in enumerate(inorder):
            val_to_i[val] = i

        def rec_build(inorder_l, inorder_r, preorder_l, preorder_r):
            if preorder_l >= len(preorder) or inorder_l > inorder_r or preorder_l > preorder_r:
                return None
            
            # The first value in the preorder array is the root
            cur_node = TreeNode(preorder[preorder_l])

            # Find the root location in the inorder array
            inorder_partition = val_to_i[cur_node.val]

            # Calculate subtree size
            subtree_size = inorder_partition - inorder_l

            cur_node.left = rec_build(inorder_l, inorder_partition - 1, preorder_l + 1, preorder_l + subtree_size)
            cur_node.right = rec_build(inorder_partition + 1, inorder_r, preorder_l + subtree_size + 1, preorder_r)
            return cur_node
        
        return rec_build(0, len(inorder) - 1, 0, len(preorder) - 1)