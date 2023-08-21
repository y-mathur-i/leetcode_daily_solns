class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l_s = len(s)
        for i in range(1, (len(s)//2)+1):
            if l_s%i == 0:
                cnt = l_s//i
                if cnt*s[:i] == s:
                    return True
        return False
