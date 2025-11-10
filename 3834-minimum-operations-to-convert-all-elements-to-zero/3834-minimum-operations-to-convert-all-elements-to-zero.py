class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        res = 0
        
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num > 0 and (not stack or num != stack[-1]):
                res += 1
                stack.append(num)
        
        return res