class Solution:
    def jump(self, nums: List[int]) -> int:
        n = 0
        f = 0
        j = 0
        while f < len(nums) - 1:
            fs = 0
            for i in range(n, f + 1):
                fs = max(fs, nums[i] + i)
            
            n = f + 1
            f = fs
            j += 1
        return j