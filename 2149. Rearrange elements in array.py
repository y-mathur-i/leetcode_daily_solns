class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]
        i = 0
        for p, n in zip(pos, neg):
            nums[i] = p
            nums[i+1] = n
            i += 2
        return nums
