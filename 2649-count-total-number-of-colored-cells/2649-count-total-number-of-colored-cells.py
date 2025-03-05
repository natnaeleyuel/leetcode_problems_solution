class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            start = 1
            cal_sum = 1
            for i in range(1, n):
                cal_sum = cal_sum + start + start + 2
                start += 2
            return cal_sum