from typing import List
from functools import lru_cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)
        @lru_cache(maxsize=None)
        def get_ans(i):
            if i >= len(s):
                return 0
            # considering current char is not part of anything
            res = 1 + get_ans(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in dict_set:
                    # as it is valid from i->j we can start with next and 
                    res = min(res, get_ans(j+1))
            return res
        return get_ans(0)