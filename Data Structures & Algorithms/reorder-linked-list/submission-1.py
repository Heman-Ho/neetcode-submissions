# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the half-way node
        slow, fast = head, head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the LL
        prev = None
        cur = slow.next
        slow.next = None

        while cur: 
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # merge the two halves
        # The two heads we need to merge are head and prev
        p2 = prev # Rename for clarity
        p1 = head
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1

            p1 = tmp1
            p2 = tmp2
      
    
