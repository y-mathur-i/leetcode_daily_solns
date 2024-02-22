class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_count = defaultdict(int)
        trustees = defaultdict(list)
        for trustee, trusted in trust:
            trusts_count[trustee] += 1
            trustees[trusted].append(trustee)
        for i in range(1, n+1):
            if trusts_count[i] == 0 and len(trustees[i]) == n-1:
                return i
        return -1
