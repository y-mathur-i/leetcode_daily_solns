class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first_p = None
        for i,e in enumerate(nums):
            if e >= 0:
                first_p = i
                break
        if first_p is None:
            return list(n**2 for n in nums)[::-1]
        if first_p == 0:
            return list(n**2 for n in nums)
        res = []
        neg = first_p - 1
        while neg >= 0 and first_p < len(nums):
            if nums[neg]**2 < nums[first_p]**2:
                res.append(nums[neg]**2)
                neg -= 1
            else:
                res.append(nums[first_p]**2)
                first_p += 1
        # print(res)
        while neg >= 0:
            res.append(nums[neg]**2)
            neg -= 1
        while first_p < len(nums):
            res.append(nums[first_p]**2)
            first_p += 1
        return res