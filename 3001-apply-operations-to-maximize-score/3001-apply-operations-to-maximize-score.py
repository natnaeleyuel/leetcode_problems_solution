class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = int(1e9 + 7)
        n = len(nums)
        ps = [0] * n

        for i in range(n):
            num = nums[i]
            for fac in range(2, int(math.sqrt(num)) + 1):
                if num % fac == 0:
                    ps[i] += 1

                    while num % fac == 0:
                        num //= fac

            if num >= 2:
                ps[i] += 1
        
        ndom = [n] * n
        pdom = [-1] * n

        stack = []
        for i in range(n):
            while stack and ps[stack[-1]] < ps[i]:
                ind = stack.pop()

                ndom[ind] = i

            if stack:
                pdom[i] = stack[-1]

            stack.append(i)
        
        numsubarr = [0] * n
        for i in range(n):
            numsubarr[i] = (ndom[i] - i) * (i - pdom[i])

        que = []
        for i in range(n):
            heapq.heappush(que, (-nums[i], i))

        score = 1
        def pw(b, expn):
            res = 1
            while expn > 0:
                if expn % 2 == 1:
                    res = (res * b) % MOD

                b = (b * b) % MOD
                expn //= 2

            return res
        
        while k > 0:
            num, ind = heapq.heappop(que)
            num = -num  

            opr = min(k, numsubarr[ind])

            score = (score * pw(num, opr)) % MOD

            k -= opr

        return score
