class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n > 0:
            n -= 1
            char = chr(ord('A') + n%26)
            res += char
            n //= 26
        return res[::-1]
