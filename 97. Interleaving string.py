class Solution:
    @lru_cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):  # if combined len is not eq it can not create the third one
            return False
        if sorted(s1+s2) != sorted(s3):  # if combined chars are not same -> it can't create it
            return False
        if not s1 and not s2:
            return True
        res = False
        if s1 and s1[0] == s3[0]:
            res |= self.isInterleave(s1[1:], s2, s3[1:])
        if s2 and s2[0] == s3[0]:
            res |= self.isInterleave(s1, s2[1:], s3[1:])
        return res
