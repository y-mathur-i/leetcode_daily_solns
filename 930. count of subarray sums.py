class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sm = 0
        res = 0
        di = {0:1}
        for r in range(len(nums)):
            sm += nums[r]
            if sm - goal in di:
                res += di[sm-goal]
            di[sm] = di.get(sm, 0) + 1

        return res 
