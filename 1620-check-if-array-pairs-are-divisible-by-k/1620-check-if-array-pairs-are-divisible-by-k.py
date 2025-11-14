class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) % k != 0:
            return False
        
        remainder_count = [0] * k
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        for i in range(1, (k // 2) + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        if k % 2 == 0:
            if remainder_count[k // 2] % 2 != 0:
                return False
        
        return remainder_count[0] % 2 == 0


        