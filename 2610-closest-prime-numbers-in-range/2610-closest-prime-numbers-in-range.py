class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            if n < 2:
                return []
            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False
            for i in range(2, isqrt(n) + 1):
                if sieve[i]:
                    sieve[i*i : n+1 : i] = [False]*len(sieve[i*i : n+1 : i])
            return [i for i, is_prime in enumerate(sieve) if is_prime]

        primes = sieve(right)
        primes = [p for p in primes if p >= left]

        if len(primes) < 2:
            return [-1, -1]

        cand1, cand2 = -1, -1
        min_diff = float('inf')
        for i in range(1, len(primes)):
            current_diff = primes[i] - primes[i-1]
            if current_diff < min_diff:
                cand1, cand2 = primes[i-1], primes[i]
                min_diff = current_diff

        return [cand1, cand2]