class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d,w in flights:
            graph[s].append((d, w))
        
        dist = [float("inf")]*n
        dist[src] = 0
        for _ in range(k+1):
            new_dist = dist[:]
            for s in range(n):
                if dist[s] != float("inf"):
                    for nei, wt in graph[s]:
                        if new_dist[nei] > dist[s] + wt:
                            new_dist[nei] = dist[s] + wt
            dist = new_dist
        return dist[dst] if dist[dst] != float("inf") else -1

