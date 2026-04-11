# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp!=None:
            temp=temp.next
            count+=1
        res=[]
        mid=count//2
        curr=-1
        prev=None
        while curr<mid:
            curr+=1
            prev=head
            head=head.next
        return prev