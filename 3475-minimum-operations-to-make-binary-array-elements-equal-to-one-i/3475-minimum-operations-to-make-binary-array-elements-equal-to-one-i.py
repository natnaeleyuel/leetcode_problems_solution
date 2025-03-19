class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_operations = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                min_operations += 1
                nums[i] = 1
                nums[i+1] = 0 if nums[i+1] else 1
                nums[i+2] = 0 if nums[i+2] else 1
        return min_operations if sum(nums) == len(nums) else -1