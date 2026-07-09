# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head 
        tmp = head.next
        prev = None

        while tmp:
            cur.next = prev
            prev = cur
            cur = tmp
            tmp = tmp.next

        cur.next = prev
        return cur