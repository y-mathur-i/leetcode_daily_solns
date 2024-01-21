class Solution:
    def rob(self, nums: List[int]) -> int:
        """

        At any given i
        -> Choose to rob
            -> Next possible : i + 2
        -> Choose NOT to rob
            -> Next possible : i + 1

        """
        @lru_cache(maxsize=None)
        def get_ans(i):
            if i >= len(nums):
                return 0
            # choose to rob
            ans = nums[i] + get_ans(i+2)
            # choose not to rob 
            ans = max(ans, get_ans(i+1))
            return ans
        return get_ans(0)
