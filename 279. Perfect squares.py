class Solution:
    def numSquares(self, n: int) -> int:
        pows = list(pow(i, 2) for i in range(int(sqrt(n))+2))

        dp = [float("inf")]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(len(dp)):
            for p in pows:
                if p <= i:
                    dp[i] = min(dp[i], 1 + dp[i-p])
        return dp[-1]
