class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        init = 1
        res = 1
        while init <= n:
            res *= init
            init += 1
        ans = 0
        while res >= 10:
            if res % 10 == 0:
                ans += 1
                res = res // 10
            else:
                break
        return ans