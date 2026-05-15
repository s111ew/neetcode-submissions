class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                prev_row = out[i-1]
                row[j] = prev_row[j-1] + prev_row[j]
            out.append(row)
        return out