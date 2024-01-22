class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        for n in nums:
            if n in seen:
                ans.append(n)
            seen.add(n)
        for i in range(1, len(nums)+1):
            if i not in seen:
                ans.append(i)
        return ans