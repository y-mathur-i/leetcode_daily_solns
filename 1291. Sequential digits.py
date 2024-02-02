class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = [i for i in range(1, 10)]
        res = []
        for i in range(len(digits)):
            curr = 0
            for j in range(i, len(digits)):
                curr = curr*10 + digits[j]
                if curr > high:
                    break
                else:
                    if curr >= low:
                        res.append(curr)
        return sorted(res)
