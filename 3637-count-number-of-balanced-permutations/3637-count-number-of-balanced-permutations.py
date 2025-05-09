class Solution:
    MOD = 10 ** 9 + 7
    def countBalancedPermutations(self, num: str) -> int:
        cnt = Counter(int(c) for c in num)
        s = sum(int(c) for c in num)

        if s % 2 != 0:
            return 0

        half = s // 2
        n = len(num)
        odd = n // 2
        even = n - odd

        @lru_cache(maxsize=None)
        def dfs(d, o, e, b):
            if o == 0 and e == 0 and b == 0:
                return 1
            if d < 0 or o < 0 or e < 0 or b < 0:
                return 0

            res = 0
            for j in range(0, cnt[d] + 1):
                ou = j
                eu = cnt[d] - j
                if ou > o or eu > e:
                    continue
                co = comb(o, ou)
                ce = comb(e, eu)
                res += co * ce * dfs(d - 1, o - ou, e - eu, b - d * ou)
                res %= self.MOD
            return res

        return dfs(9, odd, even, half)