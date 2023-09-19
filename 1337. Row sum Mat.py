from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows= list((sum(row), i) for i, row in enumerate(mat))
        rows.sort()
        return [i for s, i in rows][:k]
