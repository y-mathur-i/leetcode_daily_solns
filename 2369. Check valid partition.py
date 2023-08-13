from functools import lru_cache
from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # do a split when any on of the condiutions is satisfied ?
        # eq_tw, eq_th, seq
        @lru_cache(maxsize=None)
        def get_ans(i):
            if i < 0:
                return True
            res = False
            if i > 0 and nums[i] == nums[i-1]:
                res |= get_ans(i-2)
            if i > 1 and nums[i] == nums[i-1] == nums[i-2]:
                res |= get_ans(i-3)
            if i > 1 and nums[i] == nums[i-1] + 1 == nums[i-2] + 2:
                res |= get_ans(i-3)
            return res
        return get_ans(len(nums)-1)