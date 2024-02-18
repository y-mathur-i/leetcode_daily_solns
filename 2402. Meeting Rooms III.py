class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        This is tough
        heap => (endTime, RoomNumber)

        """
        meetings.sort()
        freq = [0]*n
        used = [] # (end, number)
        avail = [i for i in range(n)]
        for s, e in meetings:
            while used and s >= used[0][0]:
                heapq.heappush(avail, heapq.heappop(used)[1])
            if avail:
                to_use = heapq.heappop(avail)
                freq[to_use] += 1
                heapq.heappush(used, (e, to_use))
            else:
                end, no = heapq.heappop(used)
                freq[no] += 1
                heapq.heappush(used, (end + (e-s), no))
        return freq.index(max(freq))
