class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(2, n):
            max_num = nums[0]
            for j in range(1, i):
                curr = (max_num - nums[j]) * nums[i]
                result = max(result, curr)
                max_num = max(max_num, nums[j])

        return result