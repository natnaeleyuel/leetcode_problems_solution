class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor