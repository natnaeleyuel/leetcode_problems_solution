class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_nums = []
        large_nums = []
        c = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                less_nums.append(nums[i])

            if nums[i] > pivot:
                large_nums.append(nums[i])

            if nums[i] == pivot:
                c += 1
        return less_nums + [pivot]*c + large_nums