class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # binary search
        # the space is len of customers
        # validation function Nope -> as do not know what to minimise on
        # prefix sum at any point have sum of N before this point and y after this point
        y_sum = [0]
        n_sum = [0]
        for i, e in enumerate(customers):
            y_sum.append(y_sum[-1] + (e == "Y"))
            n_sum.append(n_sum[-1] + (e == "N"))
        ans = None
        res = float("inf")
        for i in range(len(customers)+1):
            n_ = n_sum[i]
            y_ = y_sum[-1] - y_sum[i]
            curr = n_ + y_
            if curr < res:
                ans = i
                res = curr
        return ans


        # return 0
        # def validate(h):
        #     cnt = 0
        #     for i, e in enumerate(customers):
        #         if i < h:
        #             cnt += e == "N"
        #         else:
        #             cnt += e == "Y"
        #     return cnt
        # res = float("inf")
        # ans = None
        # for i in range(len(customers)+1):
        #     curr = validate(i)
        #     if res > curr:
        #         res = curr
        #         ans = i
        # return ans
