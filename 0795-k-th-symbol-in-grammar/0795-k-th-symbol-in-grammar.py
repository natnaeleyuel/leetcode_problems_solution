class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recur(n, k):
            if n == 1:
                return 0
            l = 2 ** (n - 2)
            if k <= l:
                return recur(n - 1, k)
            else:
                return 1 - recur(n - 1, k - l)
        
        return recur(n, k)