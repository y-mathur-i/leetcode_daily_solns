class Solution:
    def minimumLength(self, s: str) -> int:
        """
        preff -> left_end
        suff -> right_end
        while preff[-1] == left_end:
            shift left_end
        while suff[-1] == right_end:
            shift right_end
        
        """
        l = 0
        r = len(s) - 1
        tot = len(s)
        while l < r:
            pre = s[l]
            suf = s[r]
            if pre != s[r]:
                break
            while l <= r and pre == s[l]:
                l += 1
                tot -= 1
            while l <= r and suf == s[r]:
                r -= 1
                tot -= 1
        return tot
