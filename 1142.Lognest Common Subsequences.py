class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(1, len(res)):
            for j in range(1, len(res[i])):
                if text2[i-1] == text1[j-1]:
                    res[i][j] = 1 + res[i-1][j-1]
                else:
                    res[i][j] = max(res[i-1][j-1], res[i-1][j], res[i][j-1])
        return res[-1][-1]