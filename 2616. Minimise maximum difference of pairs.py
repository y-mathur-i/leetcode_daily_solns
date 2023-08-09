class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def check(diff):
            seen_p = 0
            i = 0
            while i < len(nums)-1:
                if abs(nums[i] - nums[i+1]) <= diff:
                    i += 1
                    seen_p += 1
                i += 1
            return seen_p >= p

        l = 0
        r = 10**9 + 7
        while l < r:
            m = (l+r)//2
            if check(m):
                r = m
            else:
                l = m + 1
        return l
