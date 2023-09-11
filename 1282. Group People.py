from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # working based on there is at least one guaranteed option for an arrrangement
        res = []
        g_di = defaultdict(list)
        for i, grp in enumerate(groupSizes):
            g_di[grp].append(i)
        
        for k in sorted(g_di.keys()):
            v = g_di[k]
            st, end = 0, k-1
            while end < len(v):
                res.append(v[st:end+1])
                st, end = st + k, end + k
        return res
