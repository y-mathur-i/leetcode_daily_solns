class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        for i in reversed(range(32)):
            l,r = left&(1<<i), right&(1<<i)
            if l == r:
                res |= l
            else:
                break
        return res
