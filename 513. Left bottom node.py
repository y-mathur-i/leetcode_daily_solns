# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level_left = None
        if not root:
            return level_left
        q = deque()
        q.append(root)
        while q:
            level_left = q[0].val
            new_q = deque()
            while q:
                curr = q.popleft()
                if curr.left:
                    new_q.append(curr.left)
                if curr.right:
                    new_q.append(curr.right)
            q= new_q
        return level_left
