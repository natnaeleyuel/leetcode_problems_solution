class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        max_el = max(nums)
        result = 0
        left = 0
        window_max_el = 0

        for right in range(n):

            if nums[right] == max_el:
                window_max_el += 1

            while window_max_el == k:

                if nums[left] == max_el:
                    window_max_el -= 1
                left += 1

            result += left
        return result
