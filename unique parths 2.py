from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[-1][-1]:
            return 0
        if grid[0][0]:
            return 0
        grid[0][0] = 1
        for i in range(1, len(grid)):
            grid[i][0] = grid[i-1][0] if not grid[i][0] else 0
        
        for j in range(1, len(grid[0])):
            grid[0][j] = grid[0][j-1] if not grid[0][j] else 0
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                if not grid[i][j]:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0

        return grid[-1][-1]
