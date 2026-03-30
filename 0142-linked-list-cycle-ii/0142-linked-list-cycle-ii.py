# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                break
        if fast==None or fast.next==None:
            return None
        slow=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return fast