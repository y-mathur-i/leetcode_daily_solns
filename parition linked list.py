from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = less_ref = ListNode(-1)
        grt = grt_ref = ListNode(-1)
        while head:
            next = head.next
            head.next = None
            if head.val < x:
                less.next = head
                less = less.next
            else:
                grt.next = head
                grt = grt.next
            head = next

        less.next = grt_ref.next
        return less_ref.next
