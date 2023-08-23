class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_heap = []
        cnt = Counter(s)
        for l,f in cnt.items():
            heapq.heappush(freq_heap, (-f, l))
        res = ""
        while len(freq_heap) > 1:
            f_f, f_l = heapq.heappop(freq_heap)
            s_f, s_l = heapq.heappop(freq_heap)
            if not res or res[-1] != f_l:
                res += f_l
                f_f += 1
            else:
                res += s_l
                s_f += 1
            if f_f:
                heapq.heappush(freq_heap, (f_f, f_l))
            if s_f:
                heapq.heappush(freq_heap, (s_f, s_l))
        l_f, l_l = heapq.heappop(freq_heap)
        if l_f == -1:
            return res + l_l
        return ""
