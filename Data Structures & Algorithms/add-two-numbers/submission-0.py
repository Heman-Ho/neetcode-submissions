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
            if not cur1 and not cur2:
                res = carry_on
            elif not cur1:
                res = cur2.val + carry_on
                cur2 = cur2.next
            elif not cur2:
                res = cur1.val + carry_on
                cur1 = cur1.next
            else:
                res = cur1.val + cur2.val + carry_on
                cur1 = cur1.next
                cur2 = cur2.next

            carry_on = res // 10
            res = res % 10
            cur3.next = ListNode(res)
            cur3 = cur3.next
        
        
        
        return dummy.next

   

        
