# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def get_ans(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            l, r = get_ans(root.left), get_ans(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        get_ans(root)
        return self.res
