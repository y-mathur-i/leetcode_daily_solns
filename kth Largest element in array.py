from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # should be done with quick select but i got lazy
        return sorted(nums, reverse=True)[k-1]
