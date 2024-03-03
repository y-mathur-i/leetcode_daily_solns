# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fo = head
        while n != 0:
            fo = fo.next
            n -= 1
        so = head
        if not fo: # this means n == len(list[ListNode])
            return head.next
        while fo.next:
            fo = fo.next
            so = so.next
        so.next = so.next.next
        return head
