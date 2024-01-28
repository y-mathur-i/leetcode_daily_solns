class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        """
        -> Create a preffix sum matrix
        stating from each row
        to end row [Cascading]
        rowsum -> 
        ColSum |
        [[1,1,1],
         [1,1,1],
         [1,1,1]]
        Row wise
        [[1,2,3],
         [1,2,3],
         [1,2,3]]
        [[1,2,3],
         [2,4,6],
         [3,6,9]]
        
        """
        def get_ans(arr):
            """
            x + tar = sm
            x = sm-tar
            
            """
            di = {0:1}
            res = 0
            sm = 0
            for n in arr:
                sm += n
                if sm-target in di:
                    res += di[sm-target]
                di[sm] = di.get(sm, 0) + 1
            return res
        ans = 0
        for i in range(len(mat)):
            temp = [0 for _ in range(len(mat[i]))]
            for j in range(i, len(mat)):
                temp = [m+n for m,n in zip(temp, mat[j])]
                ans += get_ans(temp)
        return ans
