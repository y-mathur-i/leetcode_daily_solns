class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n+1):
            res ^= i
        for i in nums:
            res ^= i
        return res
