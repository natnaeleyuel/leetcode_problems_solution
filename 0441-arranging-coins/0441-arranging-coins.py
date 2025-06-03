class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 1
        while n >= i:
            n -= i
            i += 1
            count += 1
        
        return count
