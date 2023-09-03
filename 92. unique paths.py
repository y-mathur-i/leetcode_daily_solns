class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for j in range(len(dp[0])):
            dp[0][j] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
