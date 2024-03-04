class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = 0
        score = 0
        l = 0
        r = len(tokens) - 1
        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
                res = max(res, score)
            else:
                if not score:
                    return res
                else:
                    power += tokens[r]
                    score -= 1
                    r -= 1
        return res
