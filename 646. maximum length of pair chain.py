from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1 for _ in range(len(pairs))]
        for i in range(len(dp)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
