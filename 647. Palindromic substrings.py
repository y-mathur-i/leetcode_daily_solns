class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        res = len(s)
        for i in range(len(s)):
            dp[i][i] = True
        for gap in range(2, len(s)+1):
            for i in range(0, len(s)-gap + 1):
                j = i + gap - 1
                if gap == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                res += int(dp[i][j])
        return res
