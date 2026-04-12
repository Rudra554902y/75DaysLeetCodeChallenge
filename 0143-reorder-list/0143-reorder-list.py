# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        list1 = head
        s = head
        f = head

        while f.next is not None and f.next.next is not None:
            s = s.next
            f = f.next.next

        list2 = s.next
        s.next = None

        cur = list2
        prev = None
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        list2 = prev
        while list2 is not None:
            n = list1.next
            p = list2.next
            list1.next = list2
            list2.next = n
            list2 = p
            list1 = list1.next.next