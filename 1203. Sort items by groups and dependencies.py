from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # group dependencies and graph nodes dependencies
        def do_topo_sort(graph, in_deg):
            q = deque()
            res = []
            for i in graph.keys():
                if not in_deg[i]:
                    q.append(i)            
            while q:
                n = q.pop()
                res.append(n)
                for nei in graph[n]:
                    in_deg[nei] -= 1
                    if not in_deg[nei]:
                        q.append(nei)
            return res
        grp = m
        for i, g in enumerate(group):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        item_graph = {i: [] for i in range(n)}
        item_in_deg = {i: 0 for i in range(n)}
        grp_graph = {i: [] for i in range(m)}
        grp_in_deg = {i: 0 for i in range(m)}

        for d, deps in enumerate(beforeItems):
            for s in deps:
                item_graph[s].append(d)
                item_in_deg[d] += 1
                if group[s] != group[d]:
                    grp_graph[group[s]].append(group[d])
                    grp_in_deg[group[d]] += 1


        
        item_sort = do_topo_sort(item_graph, item_in_deg)
        grp_sort = do_topo_sort(grp_graph, grp_in_deg)
        if len(item_sort) != n or len(grp_sort) != m:
            return []
        grp_sorted_items = {i: [] for i in range(m)}
        for i in item_sort:
            grp_sorted_items[group[i]].append(i)

        res = []
        for g in grp_sort:
            res.extend(grp_sorted_items[g])
        return res
