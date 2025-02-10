class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            min_ind = i
            for j in range(i, len(nums)):
                if nums[min_ind] > nums[j]:
                    min_ind = j
            nums[i], nums[min_ind] = nums[min_ind], nums[i]
        return nums
        