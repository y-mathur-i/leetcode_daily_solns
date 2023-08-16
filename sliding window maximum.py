from collections import deque
from typing import List


class MaxQue:
    def __init__(self):
        self.q = deque()


    def insert(self, val, idx):
        while self.q and self.q[-1][0] < val:
            self.q.pop()
        self.q.append((val, idx))
        
    
    def remove(self, idx):
        while self.q and self.q[0][1] <= idx:
            self.q.popleft()
    
    def get_max(self):
        return self.q[0][0] if self.q else None


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MaxQue()
        for i in range(k):
            q.insert(nums[i], i)
        i = 0
        j = k
        res = []
        while j < len(nums):
            res.append(q.get_max())
            q.insert(nums[j], j)
            q.remove(i)
            i += 1
            j += 1
        res.append(q.get_max())
        return res
