from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # sliding window?
        di = {}
        sm = 0
        for i in range(k):
            di[nums[i]] = di.get(nums[i], 0) + 1
            sm += nums[i]
        r = k
        l = 0
        res = sm if len(di.keys()) >= m else 0
        while r < len(nums):
            if len(di.keys()) >= m:
                res = max(res, sm)
            di[nums[l]] -= 1
            if di[nums[l]] == 0:
                del di[nums[l]]
            di[nums[r]] = di.get(nums[r], 0) + 1
            sm -= nums[l]
            sm += nums[r]
            r += 1
            l += 1
        return max(res, sm) if len(di.keys()) >= m else res
