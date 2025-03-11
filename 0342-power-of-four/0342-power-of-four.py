class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        pow4 = 1
        while pow4 <= n:
            pow4 = 4 ** x
            if pow4 == n:
                return True
            x += 1
        return False