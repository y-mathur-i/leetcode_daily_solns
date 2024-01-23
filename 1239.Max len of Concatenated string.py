class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def to_bit_map(curr):
            mp = 0
            for l in curr:
                mp |= (1<< (ord(l) - ord('a')))
            return mp
        flt = []
        for n in arr:
            if len(set(n)) == len(n):
                flt.append(n)
        di = {n: to_bit_map(n) for n in flt}
        if not flt:
            return 0
        self.res = 0
        @lru_cache(maxsize=None)
        def get_ans(i, curr):
            if i == len(flt):
                return 0
            ans = 0
            if not curr & di[flt[i]]:
                ans += len(flt[i]) + get_ans(i+1, curr|di[flt[i]])
            ans = max(ans, get_ans(i+1, curr))
            return ans
        return get_ans(0, 0)
