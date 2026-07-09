"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a new LL and map the reference of old LL node to new LL node
        # Use that mapping to set the random 
        if not head:
            return None

        dummy = Node(0, None, None)
        traverse_orig = head
        traverse_new = dummy
        old_to_new = {}

        while traverse_orig:
            traverse_new.next = Node(traverse_orig.val, None, None)
            old_to_new[traverse_orig] = traverse_new.next
            traverse_orig = traverse_orig.next
            traverse_new = traverse_new.next

        traverse_old = head
        traverse_new = dummy.next
        while traverse_old:
            if traverse_old.random:
                traverse_new.random = old_to_new[traverse_old.random]
            traverse_old = traverse_old.next
            traverse_new = traverse_new.next
        
        return dummy.next
