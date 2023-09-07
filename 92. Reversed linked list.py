# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        nodes = []
        h = head
        while h:
            nxt = h.next
            nodes.append(h)
            h.next = None
            h = nxt
        l = nodes[:left-1]
        mid = nodes[left-1:right][::-1]
        r = nodes[right:]
        ref = n = TreeNode(-1)
        nodes = []
        nodes.extend(l)
        nodes.extend(mid)
        nodes.extend(r)
        # print(nodes)
        while nodes:
            n.next = nodes.pop(0)
            n = n.next
        return ref.next
