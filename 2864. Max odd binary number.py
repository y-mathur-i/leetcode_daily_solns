class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = s.count("1")
        return (cnt-1)*"1" + (len(s)-cnt)*"0" + "1"