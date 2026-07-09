# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_on = 0
        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        cur3 = dummy

        while cur1 or cur2 or carry_on:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            res = val1 + val2 + carry_on

            carry_on = res // 10
            res = res % 10

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
                
            cur3.next = ListNode(res)
            cur3 = cur3.next
        
        
        
        return dummy.next

   

        
