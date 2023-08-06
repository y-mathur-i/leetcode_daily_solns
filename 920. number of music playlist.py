class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0 for _ in range(n+1)] for g in range(goal+1)]
        MOD = 10**9 + 7
        dp[0][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, min(i, n) + 1):
                dp[i][j] = dp[i-1][j-1]*(n-j+1)  # prev possibilities with one less song and one less slot * (adding one more slot and one more song from available ones)
                if j > k: # we can pick some old songs
                    dp[i][j] += dp[i-1][j]*(j-k)%MOD
        return dp[goal][n]%MOD
