class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diffs = []
        sm = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                d = heights[i] - heights[i-1]
                heapq.heappush(diffs, d)
                while len(diffs) > ladders:
                    sm += heapq.heappop(diffs)
                if sm > bricks:
                    return i-1
        return len(heights)-1
