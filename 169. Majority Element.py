class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        num = nums[0]
        for n in nums[1:]:
            if num == n:
                count += 1
            else:
                count -= 1
                if not count:
                    count = 1
                    num = n
        return num