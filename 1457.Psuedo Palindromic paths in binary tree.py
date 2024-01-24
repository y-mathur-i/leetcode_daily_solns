Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        Creating path for each node into a bitmap
        if map is zero or has only one bit active .i.e power of 2
        res += 1
        """
        def get_ans(node, mp):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                curr_mp = mp
                curr_mp ^= (1<<node.val)
                if curr_mp == 0 or curr_mp&(curr_mp-1) == 0:
                    return 1
                return 0
            return get_ans(node.left, mp^(1<<node.val)) + get_ans(node.right, mp^(1<<node.val))
        return get_ans(root, 0)
            