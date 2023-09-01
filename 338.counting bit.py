class Solution:
    def countBits(self, n: int) -> List[int]:
        # every two ki power is 1
        # now every number between that range 
        #can be expressed as sum of prev numbers
        # need to write this down on notes
        res = []
        for i in range(n+1):
            m = i
            curr = 0
            while m:
                curr += m&1
                m >>= 1
            res.append(curr)
        return res
