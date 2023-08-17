class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS - each place not eq 0:
            result = 1 + min(top, bottom, left, right)
            - else:
                0
        """
        rows = len(mat)
        cols = len(mat[0])
        res = [[float("inf") if mat[j][i] else 0 for i in range(len(mat[0]))] for j in range(len(mat))]
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if not mat[i][j]:
                    q.append((0, i, j))

        while q:
            d, i, j = q.popleft()
            new_dist = d + 1
            for r,c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= r < rows and 0 <= c < cols:
                    if new_dist < res[r][c]:
                        res[r][c] = new_dist
                        q.append((new_dist, r, c))
        return res

        
#         done = set()
#         def bfs(i,j):
#             if (i, j) not in done:
#                 done.add((i, j))
#                 if mat[i][j] == 0:
#                     res[i][j] = 0
#                     return 0
#                 for r,c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
#                     if 0 <= r < rows and 0 <= c < cols:
#                         res[i][j] = min(res[i][j],  1 + bfs(r, c))
#                 return res[i][j]
#             return res[i][j]

#         rows = len(mat)
#         cols = len(mat[0])
#         for i in range(rows):
#             for j in range(cols):
#                 bfs(i, j)
#         return res