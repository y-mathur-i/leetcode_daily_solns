class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Choice ? Pick or don't pick 
        """
        @lru_cache(maxsize=None)
        def get_ans(r, c1, c2):
            if c1 == c2:
                return 0
            if r == len(grid) - 1:
                return grid[r][c1] + grid[r][c2]
            ans = 0
            curr = grid[r][c1] + grid[r][c2]
            for c in [c1+1, c1, c1-1]:
                for c_ in [c2+1, c2, c2-1]:
                    if 0 <= c < len(grid[r]) and 0 <= c_ < len(grid[r]):
                        ans = max(ans, curr + get_ans(r+1, c, c_))
            return ans
        return get_ans(0, 0, len(grid[0])-1)
