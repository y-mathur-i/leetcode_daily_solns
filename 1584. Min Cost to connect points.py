from typing import List


class Graph:
    def __init__(self, v):
        self.par = [i for i in range(v)]
        self.rank = [0]*v
    
    def find_par(self, x):
        if self.par[x] == x:
            return x
        return self.find_par(self.par[x])
    
    def union(self, x, y):
        par_x, par_y = self.find_par(x), self.find_par(y)
        if par_x == par_y:
            return True
        if self.rank[par_x] < self.rank[par_y]:
            self.par[par_x] = par_y
        elif self.rank[par_y] < self.rank[par_x]:
            self.par[par_y] = par_x
        else:
            self.rank[par_x] += 1
            self.par[par_y] = par_x

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                src = points[i]
                dst = points[j]
                wt = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, wt))
        edges.sort(key = lambda x : x[-1])
        g = Graph(len(points))
        res = 0
        for s, d, wt in edges:
            if not g.union(s, d):
                res += wt
        return res
