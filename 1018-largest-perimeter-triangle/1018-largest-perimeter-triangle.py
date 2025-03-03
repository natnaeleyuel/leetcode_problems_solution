class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_val = -float('inf')
        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a + b > c:
            max_val = a + b + c
        
        left = 1
        right = 3
        while right < len(nums):
            a = nums[left]
            b = nums[left + 1]
            c = nums[right]

            if a + b > c:
                max_val = max(max_val, a + b + c)

            left += 1
            right += 1

        return max_val if max_val != -float('inf') else 0
