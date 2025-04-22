class Solution:
    MOD = 10**9+7
    def idealArrays(self, n: int, maxValue: int) -> int:
        sieve = list(range(maxValue+1))
        for i in range(2, int(maxValue**0.5)+1):
            if sieve[i] == i: 
                for j in range(i*i, maxValue+1, i):
                    if sieve[j] == j:
                        sieve[j] = i
        
        def factors(n):
            result = defaultdict(int)
            while n > 1:
                smallest_prime = sieve[n]
                result[smallest_prime] += 1
                n //= smallest_prime
            return result
        
        ans = 0
        for i in range(1, maxValue+1):
            ways = 1
            for exp in factors(i).values():
                ways = (ways * math.comb(n - 1 + exp, exp)) % self.MOD
            ans += ways % self.MOD
        return ans % self.MOD