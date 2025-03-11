class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powFun(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = powFun(x, n // 2)
            res = res * res 
            if n % 2 == 1:
                return res * x
            return res 

        res = powFun(x, abs(n))
        return res if n > 0 else 1 / res
        