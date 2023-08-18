from typing import List
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        inCount = {i:0 for i in range(n)}
        for s,d in roads:
            graph[s].add(d)
            graph[d].add(s)
            inCount[s] += 1
            inCount[d] += 1
        res = 0
        for i in range(n):
            curr = inCount[i]
            for j in range(n):
                if i != j:
                    temp = inCount[j] if j not in graph[i] else inCount[j] - 1
                    res = max(res,temp+curr)
        return res
