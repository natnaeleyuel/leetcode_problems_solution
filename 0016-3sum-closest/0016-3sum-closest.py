class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closSum = float('inf')
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == target:
                    return curSum
                if abs(closSum - target) > abs(curSum - target):
                    closSum = curSum
                if curSum < target:
                    left += 1
                if curSum > target:
                    right -= 1
        return closSum