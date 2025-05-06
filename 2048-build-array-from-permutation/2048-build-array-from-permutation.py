class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = list(range(n))

        for i in range(n):
            result[i] = nums[nums[i]]
        
        return result
