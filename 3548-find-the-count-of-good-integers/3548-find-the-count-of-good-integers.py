class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        d = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            pint = int(s)
            if pint % k == 0:
                sorted_s = "".join(sorted(s))
                d.add(sorted_s)

        fac = [factorial(i) for i in range(n + 1)]
        result = 0
        for s in d:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                tot //= fac[x]
            result += tot
        
        return result
