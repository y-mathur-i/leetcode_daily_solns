from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # Each node can be reached by different paths
        # the paths include ? different nodes that are visited
        # I mean i can be on the same node with different done/visited
        # best way to keep track of each visited ?
        # bitmask if i visit all what will the bitmask look like 
        # for 1 node 1 which is eq to (1 << 1) - 1
        # for 2 nodes 11
        # for 3 nodes 111 and so on
        size = len(graph)
        goal = (1<<size)-1
        res = float("inf")
        for st in range(size):
            q = deque()
            q.append((st, (1<<st)))
            done = set()
            done.add((st, (1<<st)))
            lvl = 0
            ext_loop = False
            while q:
                # print(q)
                if any(goal == visi for _, visi in q):
                    res = min(res, lvl)
                    break
                new_ = deque()
                while q:
                    curr, state = q.pop()
                    for nei in graph[curr]:
                        new_st = state | ( 1 << nei)
                        if (nei, new_st) not in done:
                            done.add((nei, new_st))
                            new_.append((nei, new_st))
                q = new_
                lvl += 1
        return res
