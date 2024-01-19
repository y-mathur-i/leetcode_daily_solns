class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in reversed(range(0, len(matrix)-1)):
            for c in range(len(matrix[r])):
                ans = float("inf")
                for dx, dy in [(r+1, c-1), (r+1, c), (r+1, c+1)]:
                    if 0 <= dy < len(matrix[r]):
                        ans = min(ans, matrix[r][c] + matrix[dx][dy])
                matrix[r][c] = ans
        return min(matrix[0])

