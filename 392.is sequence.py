class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False
        s_i = 0
        t_i = 0
        for t_i in range(len(t)):
            if t[t_i] == s[s_i]:
                s_i += 1
            if s_i == len(s):
                return True
        return False
