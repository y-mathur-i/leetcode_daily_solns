from typing import List
from functools import lru_cache


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # at each posistion i can jump k-1, k, k+1
        # the thing is i dont' need to tell the amount/count of jumps it takes
        # just need to tell yes/no
        # the states become idx with k (the modulo of prev jump)
        # we start from 0, 1
        # okay the thing is
        # i can jump only on specific positions .i.e valid placements 
        # so for each index i need to know the value on it
        st_idx = {ele: i for i, ele in enumerate(stones)}
        valid_stones = set(stones)
        @lru_cache(maxsize=None)
        def get_ans(idx, k):
            if idx == len(stones) - 1:
                return True
            deltas = [k-1, k, k+1]
            if idx == 0:
                deltas = [1]
            for delta in deltas:  # size of next jumps from idx
                next_pos = stones[idx] + delta
                if next_pos in st_idx and st_idx[next_pos] != idx:  # i get stuck on point where it jumps on the same index
                    # print(idx, delta, stones[idx], next_pos)
                    if get_ans(st_idx[next_pos], delta):
                        return True
            return False
        return get_ans(0, 1)
