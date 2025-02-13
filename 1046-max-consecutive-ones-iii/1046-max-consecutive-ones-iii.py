class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left +=1

            result = max(result, right - left + 1)
        return result 