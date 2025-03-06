class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        right = -float('inf')
        for num in reversed(nums):
            if num < right:
                return True
            
            while stack and stack[-1] < num:
                right = stack.pop()

            stack.append(num)
        
        return False