class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        t_left, t_middle, t_right = 0, 1, 1
        for _ in range(n-2):
            t_left, t_middle, t_right = t_middle, t_right, t_left + t_middle + t_right
        return t_right