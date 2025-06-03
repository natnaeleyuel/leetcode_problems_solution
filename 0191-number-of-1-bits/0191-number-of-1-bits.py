class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            count += 1 if n & (1 << i) else 0
        
        return count