class Solution:
    memo = defaultdict(int)
    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        self.memo[n] = self.fib(n-1) + self.fib(n-2)

        return self.memo[n]