class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for c in coins:
            for i in range(len(dp)):
                if i >= c:
                    dp[i] += dp[i-c]
            # print(dp)
        return dp[-1]
