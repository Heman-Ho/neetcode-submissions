# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse entire list O(N)
        # Traverse from end and remove nth node (O(N))
        # Reverse entire list again

        # Count the nodes -> num_nodes. let m = num_nodes - n
        # Remove the (m+1)th node
        count = 0
        traverse = head
        while traverse:
            traverse = traverse.next
            count += 1
        
        m = count - n 
        if m == 0:
            return head.next

        traverse = head
        for i in range(m - 1):
            traverse = traverse.next
        traverse.next = traverse.next.next
        return head