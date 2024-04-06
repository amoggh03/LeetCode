# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1=c1=ListNode(0)
        d2=c2=ListNode(0)
        while head:
            if head.val<x:
                d1.next=head
                d1=d1.next

            else:
                d2.next=head
                d2=d2.next    

            head=head.next

        d2.next=None
        d1.next=c2.next
        return c1.next    