class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        if len(nums1) % 2 != 0:
            for num in nums2:
                result ^= num

        if len(nums2) % 2 != 0:
            for num in nums1:
                result ^= num
        
        return result