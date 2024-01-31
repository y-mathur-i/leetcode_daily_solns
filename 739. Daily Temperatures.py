class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stk = []
        for i, e in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < e:
                j = stk.pop()
                res[j] = i-j
            stk.append(i)
        return res
