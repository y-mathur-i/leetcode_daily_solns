from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # can travel all the routes that reach end 
        # and see the min resistence.
        # will have to visite nodes again ?
        # as the shortest no of nodes/jumps might not be the path 
        # with least resitence
        def can_reach(i, j, allowed, done):
            if i == len(heights)-1 and j == len(heights[i]) - 1:
                return True
            if (i, j) not in done:
                done.add((i, j))
                for m, n in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= m < len(heights) and 0 <= n < len(heights[m]) and abs(heights[m][n] - heights[i][j]) <= allowed:    
                        if can_reach(m, n, allowed, done):
                            return True
            return False
        l = 0
        res= -1
        r = max(max(row) for row in heights)
        while l <= r:
            m = l + (r-l)//2
            if can_reach(0, 0, m, set()):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

