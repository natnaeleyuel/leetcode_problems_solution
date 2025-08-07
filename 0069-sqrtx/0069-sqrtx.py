class Solution:
    def mySqrt(self, x: int) -> int:
        max_cand = 0
        for i in range(x + 1):
            if i * i <= x:
                max_cand = i
            else:
                break
        return max_cand