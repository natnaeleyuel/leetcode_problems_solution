class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def helper(num):
            counts = [0] * 10
            if num == 0:
                counts[0] = 1
                return tuple(counts)
            
            while num > 0:
                counts[num % 10] += 1
                num //= 10
            return tuple(counts)

        n_counts = helper(n)
        for i in range(30): 
            k = 1 << i 
            if helper(k) == n_counts:
                return True
        
        return False