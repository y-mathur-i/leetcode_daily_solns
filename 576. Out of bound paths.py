class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = pow(10, 9) + 7
        @lru_cache(maxsize=None)
        def get_ans(i, j, left):
            if not ( 0<= i < m and 0 <= j < n):
                return 1
            if not left:
                return 0
            ans = 0
            for r, c in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                ans += get_ans(r, c, left-1)
            return ans%MOD
        
        return get_ans(startRow, startColumn, maxMove)%MOD