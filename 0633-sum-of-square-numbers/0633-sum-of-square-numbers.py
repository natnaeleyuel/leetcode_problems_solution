from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))
        while a <= b:
            cand = a * a + b * b
            if cand == c:
                return True
            elif cand > c:
                b -= 1
            elif cand < c:
                a += 1
        
        return False

