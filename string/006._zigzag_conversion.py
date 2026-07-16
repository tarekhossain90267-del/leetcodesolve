class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        cur_row, step = 0, -1

        for ch in s:
            rows[cur_row] += ch
            if cur_row == 0 or cur_row == numRows - 1:
                step *= -1
            cur_row += step

        return "".join(rows)

        
