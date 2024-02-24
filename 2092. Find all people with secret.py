class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        The time at which the meeting takes place.
        Is the sequence -> sort based on time of the meeting
        If any of the meetings happening at time T(i)
        have a person that has a secret all the people will end up having it.

        """
        t_grouped = {}
        for s, d ,t in meetings:
            graph = t_grouped.get(t, defaultdict(list))
            graph[s].append(d)
            graph[d].append(s)
            t_grouped[t] = graph
        def dfs(curr, done, graph):
            if curr in done:
                return
            done.add(curr)
            for nei in graph[curr]:
                dfs(nei, done, graph)

        knows = set()
        knows.add(0)
        knows.add(firstPerson)
        for t in sorted(t_grouped.keys()):
            curr_graph = t_grouped[t]
            done = set()
            for k in curr_graph.keys():
                if k in knows:
                    dfs(k, done, curr_graph)
            for d in done:
                knows.add(d)
        return list(knows)
