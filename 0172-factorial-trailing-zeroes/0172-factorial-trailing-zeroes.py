class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n == 0 or n == 1:
                return 1
            return n * fact(n-1)
        res = fact(n)
        ans = 0
        while res % 10 == 0:
            ans += 1
            res = res // 10
        return ans