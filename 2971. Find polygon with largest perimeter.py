class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        For the nth edge:
        2,3... n-1 edges should sum more than Nth edge
        prefix sum ?
        The aim is to create largest, so increased N is good as edges are positive.
        """
        nums.sort()
        curr = sum(nums[:2])
        ans = -1
        for n in nums[2:]:
            if n < curr:
                ans = max(ans, n + curr)
            curr += n
        return ans
