# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        curr = deque()
        curr.append(root)
        def validate_level(nodes, lvl):
            if lvl%2 == 0:
                if any(n.val%2 == 0 for n in nodes):
                    return False
                prev = nodes[0]
                for i in range(1, len(nodes)):
                    if prev.val >= nodes[i].val:
                        return False
                    prev = nodes[i]
                return True
            if lvl%2 != 0:
                if any(n.val%2 for n in nodes):
                    return False
                prev = nodes[0]
                for i in range(1, len(nodes)):
                    if prev.val <= nodes[i].val:
                        return False
                    prev = nodes[i]
                return True
        lvl = 0
        while curr:
            if not validate_level(curr, lvl):
                print([n.val for n in curr], lvl)
                return False
            next_ = deque()
            while curr:
                node = curr.popleft()
                if node.left:
                    next_.append(node.left)
                if node.right:
                    next_.append(node.right)
            curr = next_
            lvl += 1
        return True
