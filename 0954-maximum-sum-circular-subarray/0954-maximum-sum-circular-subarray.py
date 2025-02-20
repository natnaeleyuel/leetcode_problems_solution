class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_maximum = nums[0] = global_minimum = nums[0]
        current_maximum = current_minimum = 0
        total = 0
        for num in nums:
            current_minimum = min(current_minimum + num, num)
            current_maximum = max(current_maximum + num, num)

            global_minimum = min(global_minimum, current_minimum)
            global_maximum = max(global_maximum, current_maximum)

            total += num
        
        return max(global_maximum, total - global_minimum) if global_maximum > 0 else global_maximum