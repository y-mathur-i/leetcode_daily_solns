class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Produce all subsets....
        Verify if it satisfies the conditions ?
        The verification process is tough....
        Use it to prune the calls
        2^1000 subsets...
                nums.sort()
        self.res = 0
        self.ans = []
        def get_subsets(i, curr):
            if len(curr) >= 2 and not (curr[-1]%curr[-2] == 0 or curr[-2]%curr[-1] == 0):
                return 
            if i >= len(nums):
                if self.res < len(curr):
                    self.ans = curr[:]
                    self.res = len(curr)
                return
            get_subsets(i+1, curr)
            get_subsets(i+1, curr + [nums[i]])
        get_subsets(0, [])
        return self.ans

        """
        nums.sort()
        max_len = 0
        max_idx = 0
        lns = [i for i in range(len(nums))]
        dp = [1]*len(nums) # find max len possible
        for i in range(1, len(nums)):
            for j in range(i):
                if not nums[i]%nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    lns[i] = j
                    if dp[i] > max_len:
                        max_idx = i
                        max_len = dp[i]
        curr = max_idx
        res = []
        while curr != lns[curr]:
            res.append(nums[curr])
            curr = lns[curr]
        res.append(nums[curr])
        return res
