class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        5, 6, 3
        5 <- 6 : 5 is still minimum
        5 <- 3 : 3 is minummum from this point in time
        let's say 
        5 is min for [0], [0, 1]
        3 is min for [0, 1, 2], [2]

        Last mein ? is entry len - entry
        Gap strategy ?

        # 5 6 3
        5 5 5 3
        6 X 6 3
        3 X X 3

        # 3 1 2 4
        3 3 1 1 1
        1 X 1 1 1 
        2 X X 2 2
        4 X X X 4
        dp > yes but memeory alot 
                # n = len(arr)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # res = 0
        # for i in range(n):
        #     dp[i][i] = arr[i]
        #     res += arr[i]%MOD

        # for le in range(2, len(arr)+1):
        #     for i in range(0, len(arr)-le+1):
        #         j = i + le - 1
        #         dp[i][j] = min(dp[i+1][j], dp[i][j-1])
        #         res += dp[i][j]%MOD

        Result at every i,j = min(result(i-1, j), result(i, j-1))
        n = len(arr)
        self.res = 0
        @lru_cache(maxsize=None)
        def get_ans(i, j):
            if j < i:
                return 0
            if i == j:
                self.res += arr[i]
                return arr[i]
            ans = min(get_ans(i+1, j), get_ans(i, j-1))
            self.res += ans%self.MOD
            return ans
        get_ans(0, n-1)
        Memory AHHHHHHHH


        left maine jahan tak min
        right mein jahan tak min
        total -> left - Curr - right
        """
        MOD = pow(10, 9) + 7
        left = [-1 for _ in range(len(arr))]
        right = [len(arr) for _ in range(len(arr))]
        stk = []
        for i, e in enumerate(arr):
            while stk and arr[stk[-1]] > e:
                j = stk.pop()
                right[j] = i
            stk.append(i)
        
        stk = []
        for i, e in enumerate(arr):
            while stk and arr[stk[-1]] > e:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        res = 0
        for n, l, r, idx in zip(arr, left, right, range(len(arr))):
            left_items = idx - l 
            right_items = r - idx
            res += n*(left_items * right_items)%MOD
        return res%MOD