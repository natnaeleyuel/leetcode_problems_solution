class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        left = 0 
        for right in range(len(nums) - 2, -1, -1):
            num = nums[right]
            if num + right >= n:
                n = right       
        return n == 0


