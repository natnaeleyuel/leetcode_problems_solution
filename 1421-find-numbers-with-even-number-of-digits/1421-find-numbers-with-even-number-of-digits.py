class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            count = 0
            while num != 0:
                num //= 10
                count += 1
            
            if not count % 2:
                result += 1
        
        return result
            