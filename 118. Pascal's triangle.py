from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # let's simulate first
        rows = []
        rows.append([1])
        if numRows == 1:
            return rows
        rows.append([1, 1])
        if numRows == 2:
            return rows
        
        for i in range(2, numRows):
            new_row = [1]
            for j in range(1, len(rows[i-1])):
                new_row.append(rows[i-1][j] + rows[i-1][j-1])
            new_row.append(1)
            rows.append(new_row)
        return rows
