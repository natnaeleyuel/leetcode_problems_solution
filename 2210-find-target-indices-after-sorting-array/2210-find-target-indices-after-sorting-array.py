class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targetIndices = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                targetIndices.append(i)
        return targetIndices
      