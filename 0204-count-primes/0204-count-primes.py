class Solution:
    def countPrimes(self, n: int) -> int:
        seen = [0] * n
        res = 0
        
        for num in range(2, n):
            if seen[num]: 
                continue
            res += 1
            seen[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
        
        return res
        