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
        nodes = {}
        nodes[None] = None
        h = head
        while h:
            if h not in nodes:
                nodes[h] = Node(h.val)
            h = h.next
        h = head
        new_h = ref = Node(-1)
        while h:
            curr, nxt, rnd = nodes[h], nodes[h.next], nodes[h.random]
            curr.next = nxt
            curr.random = rnd
            h = h.next
        return nodes[head]
